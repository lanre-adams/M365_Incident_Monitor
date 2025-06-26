# Microsoft SIEM Incident Monitor & Automated Response

## 📢 Overview

This project provides an automated monitoring and response system for Microsoft Sentinel (SIEM) focused on:

✅ Detecting **Credential Phishing** and **Twill** related incidents  
✅ Alerting IT Administrators via Email  
✅ Automatically locking affected users if the incident remains unattended for **5 days**

---

## 🛠 Features

- Connects to Microsoft Sentinel to fetch incidents via API  
- Filters for incidents labeled as **Credential Phishing** or **Twill**  
- Sends immediate Email Alerts to IT Administrators  
- Tracks unresolved incidents, locking affected users after 5 days of no acknowledgment  

---

## ⚡ Technologies

- Python 3.9+  
- Microsoft Graph API  
- Microsoft Sentinel REST API  
- SMTP for Email Alerts  

---

## 🔒 Requirements

- Azure AD Application with permissions to:  
  - Read incidents from Microsoft Sentinel  
  - Manage Users via Microsoft Graph API  

- SMTP Email Credentials for sending alerts  

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

1. Configure credentials in `src/config.py`

```python
# Microsoft Graph & Sentinel Configuration
CLIENT_ID = "your-azure-app-client-id"
CLIENT_SECRET = "your-app-secret"
TENANT_ID = "your-tenant-id"
SUBSCRIPTION_ID = "your-subscription-id"
RESOURCE_GROUP = "your-resource-group"
WORKSPACE_NAME = "your-sentinel-workspace"

# Email Settings
SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587
EMAIL_USERNAME = "alert@yourdomain.com"
EMAIL_PASSWORD = "your-email-password"
ADMIN_EMAIL = "it-admin@yourdomain.com"
```

2. Run the monitoring script:

```bash
python src/main.py
```

**Recommendation:** Set up as a scheduled job (e.g., cron or Azure Function) to run continuously or at desired intervals.

---

## 📬 Email Alert Example

```
Subject: 🚨 Credential Phishing Incident Detected

Incident ID: 12345  
Type: Credential Phishing  
User Affected: user@example.com  
Detected On: 2025-06-26 09:15 UTC  

Action Required: Please investigate this incident. The user account will be locked automatically if no action is taken within 5 days.
```

---

## 🔐 Automatic Lock Action

If an incident remains unacknowledged after 5 days:

✅ Affected user account is disabled via Microsoft Graph API  
✅ Final email alert sent to IT Admin notifying the lockdown  

---

## 📂 Project Structure

```
src/
├── main.py             # Entry point, coordinates monitoring & response  
├── email_alert.py      # Handles sending email alerts  
├── user_lockdown.py    # Manages user lockdown after time threshold  
├── sentinel_monitor.py # Fetches and filters incidents from Sentinel  
├── config.py           # Configuration file for credentials & settings  
```

---

## 📄 License

[MIT License](LICENSE)

---

## 🤝 Contributions

Contributions, issues, and feature requests are welcome!  
Please submit a pull request or open an issue.

---

## 👨‍💻 Disclaimer

This project is intended for educational and operational use.  
Use responsibly and ensure compliance with your organization's policies.
