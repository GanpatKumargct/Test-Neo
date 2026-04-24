from sqlalchemy.orm import Session
from app.infrastructure.db.models import Lead, Interaction
from app.domain.leads.schemas import LeadCreate, LeadUpdate, InteractionCreate

def get_lead(db: Session, lead_id: int):
    return db.query(Lead).filter(Lead.id == lead_id).first()

def get_leads(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Lead).offset(skip).limit(limit).all()

def create_lead(db: Session, lead: LeadCreate):
    db_lead = Lead(**lead.model_dump())
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead

def update_lead(db: Session, lead_id: int, lead_update: LeadUpdate):
    db_lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if db_lead:
        update_data = lead_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_lead, key, value)
        db.commit()
        db.refresh(db_lead)
    return db_lead

def delete_lead(db: Session, lead_id: int):
    db_lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if db_lead:
        db.delete(db_lead)
        db.commit()
        return True
    return False

def create_interaction(db: Session, interaction: InteractionCreate):
    db_interaction = Interaction(**interaction.model_dump())
    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)
    return db_interaction

def get_interactions(db: Session, lead_id: int):
    return db.query(Interaction).filter(Interaction.lead_id == lead_id).order_by(Interaction.created_at.desc()).all()
