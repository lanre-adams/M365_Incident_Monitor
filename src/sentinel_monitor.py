import requests
from config import TENANT_ID, CLIENT_ID, CLIENT_SECRET, SUBSCRIPTION_ID, RESOURCE_GROUP, WORKSPACE_NAME

def fetch_incidents():
    token = get_access_token()
    url = f"https://management.azure.com/subscriptions/{SUBSCRIPTION_ID}/resourceGroups/{RESOURCE_GROUP}/providers/Microsoft.OperationalInsights/workspaces/{WORKSPACE_NAME}/providers/Microsoft.SecurityInsights/incidents?api-version=2022-12-01-preview"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    incidents = []
    for item in response.json().get("value", []):
        incidents.append({
            "id": item["name"],
            "type": item["properties"].get("title", ""),
            "user": item["properties"].get("owner", {}).get("assignedTo", ""),
            "detected_on": item["properties"].get("createdTimeUtc", "")
        })
    return incidents

def get_access_token():
    url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
    payload = {
        "client_id": CLIENT_ID,
        "scope": "https://management.azure.com/.default",
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials"
    }
    response = requests.post(url, data=payload)
    return response.json().get("access_token")
