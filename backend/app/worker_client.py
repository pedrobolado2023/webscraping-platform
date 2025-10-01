import redis
import json
from datetime import datetime
from app.database import SessionLocal
from app.models import JobResult

redis_client = redis.Redis.from_url("redis://redis:6379/0", decode_responses=True)

def schedule_job(job_id: int):
    """Schedule a job for execution by worker"""
    task = {
        "job_id": job_id,
        "timestamp": str(datetime.utcnow())
    }
    redis_client.lpush("job_queue", json.dumps(task))

def create_job_result(job_id: int, status: str, **kwargs):
    """Create job result in database"""
    db = SessionLocal()
    try:
        result = JobResult(
            job_id=job_id,
            status=status,
            **kwargs
        )
        db.add(result)
        db.commit()
        return result
    finally:
        db.close()