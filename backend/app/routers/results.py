from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import JobResult, User, Job
from app.schemas import JobResult as JobResultSchema
from app.routers.auth import get_current_user

router = APIRouter()

@router.get("/jobs/{job_id}/results", response_model=List[JobResultSchema])
def get_job_results(job_id: int, limit: int = 50, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Verify job ownership
    job = db.query(Job).filter(Job.id == job_id, Job.owner_id == current_user.id).first()
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    
    results = db.query(JobResult).filter(JobResult.job_id == job_id).order_by(JobResult.created_at.desc()).limit(limit).all()
    return results

@router.get("/results/{result_id}", response_model=JobResultSchema)
def get_result(result_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    result = db.query(JobResult).join(Job).filter(
        JobResult.id == result_id,
        Job.owner_id == current_user.id
    ).first()
    
    if result is None:
        raise HTTPException(status_code=404, detail="Result not found")
    
    return result