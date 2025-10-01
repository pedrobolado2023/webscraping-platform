# Backend

FastAPI REST API for authentication, job management, and result storage.

## Setup
- Install dependencies: `pip install -r requirements.txt`
- Start server: `uvicorn app.main:app --reload`
- API at `http://localhost:8000`

## Features
- JWT authentication, Google OAuth (optional)
- Job CRUD, scheduling, secure credential storage
- REST endpoints for jobs/results
- PostgreSQL for results, Redis for queue
- AES encryption for credentials (Vault/KMS optional)

## Environment Variables
- `DATABASE_URL`, `REDIS_URL`, `SECRET_KEY`, etc.
- See `.env.example` for details

## Seeding Example Jobs
- Run seed script to populate jobs from `examples/jobs_seed.json`

## Security
- Credentials encrypted at rest
- Do not store plaintext passwords

## Legal
- Do not use for unauthorized scraping
