# Worker

Playwright-based scraping engine for executing jobs asynchronously.

## Setup
- Install dependencies: `pip install -r requirements.txt` (or `npm install` if Node)
- Start worker: `python worker.py` (or `node worker.js`)

## Features
- Executes jobs from Redis queue
- Supports authenticated sessions (form, cookie, OAuth)
- Extracts and normalizes data
- Stores results in PostgreSQL
- Optional: integrates with LLM for advanced extraction

## Environment Variables
- `DATABASE_URL`, `REDIS_URL`, etc.
- See `.env.example` for details

## Testing
- Basic unit tests for scraping/parsing
