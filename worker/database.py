import os
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func
from contextlib import contextmanager

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/webscraping")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    jobs = relationship("Job", back_populates="owner")

class Job(Base):
    __tablename__ = "jobs"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    login_method = Column(String, default="none")  # none, form, oauth, cookie
    credentials_id = Column(String, nullable=True)  # encrypted reference
    script = Column(Text, nullable=True)
    schedule = Column(String, default="manual")  # manual, daily, hourly
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="jobs")
    results = relationship("JobResult", back_populates="job")

class JobResult(Base):
    __tablename__ = "job_results"
    
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, nullable=False)  # success, error, running
    structured_data = Column(Text, nullable=True)  # JSON string
    raw_html = Column(Text, nullable=True)
    screenshot_url = Column(String, nullable=True)
    logs = Column(Text, nullable=True)
    execution_time = Column(Integer, nullable=True)  # seconds
    error_message = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    job_id = Column(Integer, ForeignKey("jobs.id"))
    job = relationship("Job", back_populates="results")

@contextmanager
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()