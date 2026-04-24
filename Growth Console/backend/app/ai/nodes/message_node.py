from app.ai.graph.state import LeadProcessingState
from app.ai.providers.llm_client import get_llm
from langchain_core.prompts import PromptTemplate
import os
import re

def message_node(state: LeadProcessingState) -> LeadProcessingState:
    if not os.getenv("GROQ_API_KEY"):
        state["email_draft"] = f"Hi {state.get('name', 'there')},\n\nI loved what you're doing at {state.get('company', 'your company')}. Let's chat!"
        return state

    try:
        llm = get_llm()
        # Generate Email
        prompt_email = PromptTemplate.from_template(
            "Write a highly personalized, engaging cold email for {name} at {company}. Role: {role}. Website context: {website_summary}. Do not include subject line. Keep it under 4 sentences. Make it relevant to their role and context."
        )
        chain_email = prompt_email | llm
        res_email = chain_email.invoke({
            "name": state.get("name", "there"), 
            "company": state.get("company", "your company"), 
            "role": state.get("role", ""),
            "website_summary": state.get("website_summary", "No context")
        })
        state["email_draft"] = re.sub(r'<think>.*?</think>', '', res_email.content, flags=re.DOTALL).strip()
        
        # Generate LinkedIn
        prompt_linkedin = PromptTemplate.from_template(
            "Write a short, casual LinkedIn connection request message for {name} at {company}. Role: {role}. Mention TestNeo for API testing automation. Keep it under 3 sentences, like a quick catch up. Example format: 'Hi [Name], saw your work in QA at [Company]. We're building TestNeo for API testing automation—thought it might be relevant. Open to a quick demo?'"
        )
        chain_linkedin = prompt_linkedin | llm
        res_linkedin = chain_linkedin.invoke({
            "name": state.get("name", "there").split()[0], # Use first name
            "company": state.get("company", "your company"), 
            "role": state.get("role", "QA")
        })
        state["linkedin_draft"] = re.sub(r'<think>.*?</think>', '', res_linkedin.content, flags=re.DOTALL).strip()
        
    except Exception as e:
        state["error"] = f"Message generation error: {e}"
        state["email_draft"] = f"Hi {state.get('name', 'there')},\n\nError generating message."
        state["linkedin_draft"] = "Error generating LinkedIn message."

    return state
