import os
import json
import asyncio
from typing import Dict, Any, Optional
from playwright.async_api import async_playwright, Page, Browser
from datetime import datetime

class ScrapingEngine:
    def __init__(self):
        self.screenshots_dir = "/app/screenshots"
        os.makedirs(self.screenshots_dir, exist_ok=True)
    
    async def scrape(self, job) -> Dict[str, Any]:
        """Main scraping method"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            try:
                page = await browser.new_page()
                
                # Navigate to target URL
                await page.goto(job.url)
                await page.wait_for_load_state('networkidle')
                
                # Handle authentication if needed
                if job.login_method != "none" and job.credentials_id:
                    await self._handle_authentication(page, job)
                
                # Execute custom script if provided
                structured_data = {}
                if job.script:
                    structured_data = await self._execute_script(page, job.script)
                else:
                    # Default extraction: get page title and text content
                    structured_data = await self._default_extraction(page)
                
                # Take screenshot
                screenshot_filename = f"job_{job.id}_{int(datetime.utcnow().timestamp())}.png"
                screenshot_path = os.path.join(self.screenshots_dir, screenshot_filename)
                await page.screenshot(path=screenshot_path, full_page=True)
                
                # Get raw HTML
                raw_html = await page.content()
                
                return {
                    "structured_data": structured_data,
                    "raw_html": raw_html,
                    "screenshot_url": f"/screenshots/{screenshot_filename}"
                }
                
            finally:
                await browser.close()
    
    async def _handle_authentication(self, page: Page, job):
        """Handle different authentication methods"""
        if job.login_method == "form":
            # This is a simplified example - in production, you'd decrypt credentials
            # and implement proper form filling logic
            await self._handle_form_login(page, job)
        elif job.login_method == "cookie":
            # Handle cookie-based authentication
            await self._handle_cookie_auth(page, job)
        # Add more authentication methods as needed
    
    async def _handle_form_login(self, page: Page, job):
        """Handle form-based login"""
        # This is a placeholder - implement actual form login logic
        # based on the target site's login form structure
        pass
    
    async def _handle_cookie_auth(self, page: Page, job):
        """Handle cookie-based authentication"""
        # This is a placeholder - implement cookie setting logic
        pass
    
    async def _execute_script(self, page: Page, script: str) -> Dict[str, Any]:
        """Execute custom JavaScript extraction script"""
        try:
            # Execute the custom script in the page context
            result = await page.evaluate(script)
            return result if isinstance(result, dict) else {"result": result}
        except Exception as e:
            return {"error": f"Script execution failed: {str(e)}"}
    
    async def _default_extraction(self, page: Page) -> Dict[str, Any]:
        """Default extraction when no custom script is provided"""
        title = await page.title()
        
        # Extract basic page information
        extraction_script = """
        () => {
            return {
                title: document.title,
                url: window.location.href,
                paragraphs: Array.from(document.querySelectorAll('p')).map(p => p.textContent.trim()).filter(text => text.length > 0),
                links: Array.from(document.querySelectorAll('a[href]')).map(a => ({
                    text: a.textContent.trim(),
                    href: a.href
                })).slice(0, 10),  // Limit to first 10 links
                headings: Array.from(document.querySelectorAll('h1, h2, h3')).map(h => ({
                    level: h.tagName.toLowerCase(),
                    text: h.textContent.trim()
                }))
            }
        }
        """
        
        return await page.evaluate(extraction_script)