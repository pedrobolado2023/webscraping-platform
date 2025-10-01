from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Any
from datetime import datetime

# User schemas
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# Job schemas
class JobBase(BaseModel):
    name: str
    url: str
    login_method: str = "none"
    credentials_id: Optional[str] = None
    script: Optional[str] = None
    schedule: str = "manual"
    is_active: bool = True

class JobCreate(JobBase):
    pass

class JobUpdate(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None
    login_method: Optional[str] = None
    credentials_id: Optional[str] = None
    script: Optional[str] = None
    schedule: Optional[str] = None
    is_active: Optional[bool] = None

class Job(JobBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

# Job Result schemas
class JobResultBase(BaseModel):
    status: str
    structured_data: Optional[Dict[str, Any]] = None
    raw_html: Optional[str] = None
    screenshot_url: Optional[str] = None
    logs: Optional[str] = None
    execution_time: Optional[int] = None
    error_message: Optional[str] = None

class JobResult(JobResultBase):
    id: int
    job_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None