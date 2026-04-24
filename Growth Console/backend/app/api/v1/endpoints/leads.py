from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.infrastructure.db.session import get_db
from app.domain.leads import schemas, service

router = APIRouter()

@router.post("/", response_model=schemas.Lead)
def create_lead(lead: schemas.LeadCreate, db: Session = Depends(get_db)):
    return service.create_lead(db=db, lead=lead)

@router.get("/", response_model=List[schemas.Lead])
def read_leads(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    leads = service.get_leads(db, skip=skip, limit=limit)
    return leads

@router.get("/{lead_id}", response_model=schemas.Lead)
def read_lead(lead_id: int, db: Session = Depends(get_db)):
    db_lead = service.get_lead(db, lead_id=lead_id)
    if db_lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")
    return db_lead

@router.put("/{lead_id}", response_model=schemas.Lead)
def update_lead(lead_id: int, lead: schemas.LeadUpdate, db: Session = Depends(get_db)):
    db_lead = service.update_lead(db, lead_id, lead)
    if db_lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")
    return db_lead

@router.delete("/{lead_id}")
def delete_lead(lead_id: int, db: Session = Depends(get_db)):
    success = service.delete_lead(db, lead_id)
    if not success:
        raise HTTPException(status_code=404, detail="Lead not found")
    return {"ok": True}

@router.post("/{lead_id}/interactions", response_model=schemas.Interaction)
def create_interaction(lead_id: int, interaction: schemas.InteractionBase, db: Session = Depends(get_db)):
    interaction_create = schemas.InteractionCreate(**interaction.model_dump(), lead_id=lead_id)
    return service.add_interaction(db, interaction=interaction_create)

@router.get("/{lead_id}/interactions", response_model=List[schemas.Interaction])
def read_interactions(lead_id: int, db: Session = Depends(get_db)):
    return service.get_interactions(db, lead_id=lead_id)
