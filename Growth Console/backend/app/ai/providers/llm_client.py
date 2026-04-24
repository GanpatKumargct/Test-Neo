from langchain_groq import ChatGroq
from app.core.config import settings

def get_llm():
    if not settings.GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY not set")
    
    return ChatGroq(
        groq_api_key=settings.GROQ_API_KEY,
        model_name="qwen/qwen3-32b"
    )
