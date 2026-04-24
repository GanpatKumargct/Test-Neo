from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from datetime import date, datetime

class LeadBase(BaseModel):
    name: str
    role: Optional[str] = None
    company: str
    linkedin_url: Optional[str] = None
    website: Optional[str] = None
    notes: Optional[str] = None

class LeadCreate(LeadBase):
    pass

class LeadUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    company: Optional[str] = None
    status: Optional[str] = None
    score: Optional[int] = None
    relevant: Optional[str] = None
    score_reason: Optional[str] = None
    website_summary: Optional[str] = None
    last_contacted: Optional[date] = None

class InteractionBase(BaseModel):
    note: str

class InteractionCreate(InteractionBase):
    lead_id: int

class Interaction(InteractionBase):
    id: int
    lead_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class Lead(LeadBase):
    id: int
    status: str
    last_contacted: Optional[date] = None
    score: Optional[int] = None
    relevant: Optional[str] = None
    score_reason: Optional[str] = None
    website_summary: Optional[str] = None

    class Config:
        from_attributes = True
