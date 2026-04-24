from sqlalchemy.orm import Session
from app.domain.leads import repository, schemas

def get_lead(db: Session, lead_id: int):
    return repository.get_lead(db, lead_id)

def get_leads(db: Session, skip: int = 0, limit: int = 100):
    return repository.get_leads(db, skip=skip, limit=limit)

def create_lead(db: Session, lead: schemas.LeadCreate):
    return repository.create_lead(db, lead)

def update_lead(db: Session, lead_id: int, lead_update: schemas.LeadUpdate):
    return repository.update_lead(db, lead_id, lead_update)

def delete_lead(db: Session, lead_id: int):
    return repository.delete_lead(db, lead_id)

def add_interaction(db: Session, interaction: schemas.InteractionCreate):
    return repository.create_interaction(db, interaction)

def get_interactions(db: Session, lead_id: int):
    return repository.get_interactions(db, lead_id)
