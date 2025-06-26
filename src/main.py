from sentinel_monitor import fetch_incidents
from email_alert import send_alert
from user_lockdown import lock_user_if_needed

def main():
    incidents = fetch_incidents()
    for incident in incidents:
        if incident['type'] in ["Credential Phishing", "Twill"]:
            send_alert(incident)
            lock_user_if_needed(incident)

if __name__ == "__main__":
    main()
