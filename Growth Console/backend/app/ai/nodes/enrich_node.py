from app.ai.graph.state import LeadProcessingState
from app.ai.providers.llm_client import get_llm
from langchain_core.prompts import PromptTemplate
import os
import requests
from bs4 import BeautifulSoup

def scrape_website(url: str) -> str:
    if not url:
        return ""
    try:
        if not url.startswith("http"):
            url = "https://" + url
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        # get text from paragraphs and headings
        text = ' '.join([p.text for p in soup.find_all(['p', 'h1', 'h2', 'h3'])])
        return text[:1000] # return first 1000 chars to save tokens
    except:
        return ""

def enrich_node(state: LeadProcessingState) -> LeadProcessingState:
    website_url = state.get("website", "")
    
    if not os.getenv("GROQ_API_KEY"):
        state["website_summary"] = "Mocked enrichment - setup GROQ_API_KEY for real AI."
        return state

    if not website_url:
        state["website_summary"] = "No website provided."
        return state

    scraped_content = scrape_website(website_url)
    if not scraped_content:
        state["website_summary"] = "Failed to scrape or site empty."
        return state

    try:
        llm = get_llm()
        prompt = PromptTemplate.from_template(
            "Analyze the following website content for {company} and summarize their tech stack and potential testing needs in 3 sentences. Content: {content}"
        )
        chain = prompt | llm
        res = chain.invoke({
            "company": state.get("company", "the company"),
            "content": scraped_content
        })
        state["website_summary"] = res.content
    except Exception as e:
        state["error"] = f"Enrichment error: {e}"
        state["website_summary"] = "Error enriching website data."

    return state
