import requests
from datetime import datetime, timedelta
from config import TENANT_ID, CLIENT_ID, CLIENT_SECRET

def lock_user_if_needed(incident):
    detected_on = datetime.strptime(incident['detected_on'], "%Y-%m-%dT%H:%M:%SZ")
    if datetime.utcnow() - detected_on > timedelta(days=5):
        token = get_access_token()
        url = f"https://graph.microsoft.com/v1.0/users/{incident['user']}/accountEnabled"
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        data = {"accountEnabled": False}
        requests.patch(url, json=data, headers=headers)

def get_access_token():
    url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
    payload = {
        "client_id": CLIENT_ID,
        "scope": "https://graph.microsoft.com/.default",
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials"
    }
    response = requests.post(url, data=payload)
    return response.json().get("access_token")
