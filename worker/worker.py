import os
import json
import redis
import asyncio
import logging
from datetime import datetime
from playwright.async_api import async_playwright
from database import get_db_session, Job, JobResult
from scraper import ScrapingEngine

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Worker:
    def __init__(self):
        self.redis_url = os.getenv("REDIS_URL", "redis://redis:6379/0")
        self.redis_client = redis.Redis.from_url(self.redis_url, decode_responses=True)
        self.scraper = ScrapingEngine()
        
    async def run(self):
        logger.info("Worker started, waiting for jobs...")
        
        while True:
            try:
                # Get job from queue (blocking pop with timeout)
                job_data = self.redis_client.brpop("job_queue", timeout=10)
                
                if job_data:
                    _, job_json = job_data
                    job_info = json.loads(job_json)
                    await self.process_job(job_info["job_id"])
                    
            except Exception as e:
                logger.error(f"Worker error: {e}")
                await asyncio.sleep(5)
    
    async def process_job(self, job_id: int):
        logger.info(f"Processing job {job_id}")
        start_time = datetime.utcnow()
        
        with get_db_session() as db:
            # Get job details
            job = db.query(Job).filter(Job.id == job_id).first()
            if not job:
                logger.error(f"Job {job_id} not found")
                return
            
            # Create initial result record
            result = JobResult(
                job_id=job_id,
                status="running",
                logs=f"Started execution at {start_time}"
            )
            db.add(result)
            db.commit()
            db.refresh(result)
            
            try:
                # Execute scraping
                scrape_result = await self.scraper.scrape(job)
                
                # Calculate execution time
                execution_time = int((datetime.utcnow() - start_time).total_seconds())
                
                # Update result with success
                result.status = "success"
                result.structured_data = json.dumps(scrape_result.get("structured_data", {}))
                result.raw_html = scrape_result.get("raw_html")
                result.screenshot_url = scrape_result.get("screenshot_url")
                result.execution_time = execution_time
                result.logs += f"\nCompleted successfully at {datetime.utcnow()}"
                
                db.commit()
                logger.info(f"Job {job_id} completed successfully")
                
            except Exception as e:
                # Update result with error
                result.status = "error"
                result.error_message = str(e)
                result.execution_time = int((datetime.utcnow() - start_time).total_seconds())
                result.logs += f"\nError occurred: {e}"
                
                db.commit()
                logger.error(f"Job {job_id} failed: {e}")

if __name__ == "__main__":
    worker = Worker()
    asyncio.run(worker.run())