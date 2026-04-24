from typing import TypedDict, Optional

class LeadProcessingState(TypedDict):
    # Inputs
    lead_id: int
    name: str
    role: str
    company: str
    website: str
    notes: str
    
    # State / Outputs
    score: Optional[int]
    relevant: Optional[str]
    score_reason: Optional[str]
    website_summary: Optional[str]
    email_draft: Optional[str]
    linkedin_draft: Optional[str]
    
    # Error handling
    error: Optional[str]
