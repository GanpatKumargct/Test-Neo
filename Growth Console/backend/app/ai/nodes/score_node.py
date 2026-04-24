from app.ai.graph.state import LeadProcessingState
from app.ai.providers.llm_client import get_llm
from langchain_core.prompts import PromptTemplate
import os
import re

def score_lead_node(state: LeadProcessingState) -> LeadProcessingState:
    if not os.getenv("GROQ_API_KEY"):
        state["score"] = 8
        state["relevant"] = "Yes"
        state["score_reason"] = "Mocked score - setup GROQ_API_KEY for real AI."
        return state

    try:
        llm = get_llm()
        prompt = PromptTemplate.from_template(
            "Score this lead from 1-10 based on relevance. Role: {role}, Company: {company}, Notes: {notes}. Return just the score (number), Yes/No for relevance, and 1 sentence reason separated by |."
        )
        chain = prompt | llm
        res = chain.invoke({
            "role": state.get("role", ""), 
            "company": state.get("company", ""), 
            "notes": state.get("notes", "")
        })
        
        content = re.sub(r'<think>.*?</think>', '', res.content, flags=re.DOTALL).strip()
        parts = content.split("|")
        state["score"] = int(parts[0].strip()) if parts[0].strip().isdigit() else 7
        state["relevant"] = parts[1].strip() if len(parts) > 1 else "Yes"
        state["score_reason"] = parts[2].strip() if len(parts) > 2 else res.content
    except Exception as e:
        print(f"CRITICAL LLM ERROR: {repr(e)}")
        state["error"] = f"Scoring error: {e}"
        state["score"] = 5
        state["relevant"] = "Unknown"
        state["score_reason"] = "Error connecting to LLM"
        
    return state
