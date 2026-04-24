from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.db.session import get_db
from app.domain.leads import service as lead_service
from app.domain.leads.schemas import LeadUpdate
from pydantic import BaseModel
from app.ai.graph.builder import lead_processing_graph
from app.ai.graph.state import LeadProcessingState

router = APIRouter()

class AIMessageRequest(BaseModel):
    website_summary: str = ""

@router.post("/{lead_id}/process")
def process_lead(lead_id: int, db: Session = Depends(get_db)):
    """Run full LangGraph pipeline: Score -> Enrich -> Message"""
    db_lead = lead_service.get_lead(db, lead_id)
    if not db_lead:
        raise HTTPException(status_code=404, detail="Lead not found")
        
    initial_state = LeadProcessingState(
        lead_id=db_lead.id,
        name=db_lead.name,
        role=db_lead.role or "",
        company=db_lead.company,
        website=db_lead.website or "",
        notes=db_lead.notes or "",
        score=None,
        relevant=None,
        score_reason=None,
        website_summary=None,
        email_draft=None,
        error=None
    )
    
    final_state = lead_processing_graph.invoke(initial_state)
    
    # Update DB with new info
    update_data = LeadUpdate(
        score=final_state.get("score"),
        relevant=final_state.get("relevant"),
        score_reason=final_state.get("score_reason"),
        website_summary=final_state.get("website_summary")
    )
    lead_service.update_lead(db, lead_id, update_data)
    
    return {
        "score": final_state.get("score"),
        "relevant": final_state.get("relevant"),
        "reason": final_state.get("score_reason"),
        "website_summary": final_state.get("website_summary"),
        "email": final_state.get("email_draft"),
        "linkedin": final_state.get("linkedin_draft"),
        "error": final_state.get("error")
    }

@router.post("/{lead_id}/score")
def score_lead(lead_id: int, db: Session = Depends(get_db)):
    """Legacy individual endpoint, now triggers full process for simplicity or could just return DB data"""
    res = process_lead(lead_id, db)
    return {"score": res["score"], "relevant": res["relevant"], "reason": res["reason"]}

@router.post("/{lead_id}/generate-message")
def generate_message(lead_id: int, request: AIMessageRequest, db: Session = Depends(get_db)):
    """Legacy individual endpoint, returns existing draft or re-runs"""
    db_lead = lead_service.get_lead(db, lead_id)
    if not db_lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    
    if not db_lead.website_summary or not db_lead.score:
        res = process_lead(lead_id, db)
        return {"email": res["email"], "linkedin": res["linkedin"]}
        
    # Just run message node manually or return existing logic
    # For now, let's just trigger full process to guarantee fresh draft
    res = process_lead(lead_id, db)
    return {"email": res["email"], "linkedin": res["linkedin"]}
