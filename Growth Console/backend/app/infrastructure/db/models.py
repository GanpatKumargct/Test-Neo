from sqlalchemy import Column, Integer, String, Text, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.db.session import Base
from datetime import datetime

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role = Column(String)
    company = Column(String, index=True)
    linkedin_url = Column(String)
    website = Column(String)
    notes = Column(Text)
    status = Column(String, default="New")
    last_contacted = Column(Date, nullable=True)
    
    score = Column(Integer, nullable=True)
    relevant = Column(String, nullable=True)
    score_reason = Column(Text, nullable=True)
    website_summary = Column(Text, nullable=True)

    interactions = relationship("Interaction", back_populates="lead", cascade="all, delete-orphan")

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    lead_id = Column(Integer, ForeignKey("leads.id"))
    note = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    lead = relationship("Lead", back_populates="interactions")
