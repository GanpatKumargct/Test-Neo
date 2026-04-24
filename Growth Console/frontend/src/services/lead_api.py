import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000/api/v1")
if not BACKEND_URL.endswith("/api/v1"):
    BACKEND_URL = f"{BACKEND_URL.rstrip('/')}/api/v1"

def get_leads():
    try:
        response = requests.get(f"{BACKEND_URL}/leads/")
        if response.status_code == 200:
            return response.json()
        return []
    except Exception as e:
        print(f"Error fetching leads: {e}")
        return []

def create_lead(lead_data):
    try:
        response = requests.post(f"{BACKEND_URL}/leads/", json=lead_data)
        return response.json() if response.status_code == 200 else None
    except Exception as e:
        print(f"Error creating lead: {e}")
        return None

def update_lead(lead_id, lead_data):
    try:
        response = requests.put(f"{BACKEND_URL}/leads/{lead_id}", json=lead_data)
        return response.json() if response.status_code == 200 else None
    except Exception as e:
        print(f"Error updating lead: {e}")
        return None

def score_lead(lead_id):
    try:
        response = requests.post(f"{BACKEND_URL}/ai/{lead_id}/score")
        return response.json() if response.status_code == 200 else None
    except Exception as e:
        print(f"Error scoring lead: {e}")
        return None

def generate_message(lead_id):
    try:
        response = requests.post(f"{BACKEND_URL}/ai/{lead_id}/generate-message", json={"website_summary": ""})
        return response.json() if response.status_code == 200 else None
    except Exception as e:
        print(f"Error generating message: {e}")
        return None
