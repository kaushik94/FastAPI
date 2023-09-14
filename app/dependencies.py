import requests
import json
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    master_username: str
    master_password: str
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


BASE_URL = "https://moneysavehelp.zendesk.com/api/v2"
WEBHOOK_PAYLOAD = """{
    "webhook": {
      "name": "TEST_WEBHOOK_CREATION_VIA_FASTAPI",
      "status": "active",
      "endpoint": "https://fastapi-production-16e7.up.railway.app/webhook",
      "http_method": "POST",
      "request_format": "json",
      "subscriptions": [
        "conditional_ticket_events"
      ]
    }
}"""
TRIGGER_PAYLOAD = """{
    "trigger": {
        "title": "Roger Wilco",
        "conditions": {
            "all": [
                {
                    "field": "comment_is_public",
                    "value": "not_relevant" 
                }
            ]},
        "actions": [{ "field": "notification_webhook", "value": "%s" }],
        "category_id": "13489459478941"
    }
}"""
INSTALL_NEW_UPDATES_HTML = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Sample Form</title>
    </head>
    <body>
    <form method="post" action="/install_update">
        <a>Install new updates</a>
        <input value="install" type="submit">
    </form>
    </body>
    </html>
"""
INSTALL_UPDATES_SUCCESSFUL = """
    <body>
        <p>updates installed</p>
        <p> Following updates have been installed </p>
        <ul>
            <li> installed new webhook </li>
            <li> installed new trigger for webhook </li>
        <ul>
    </body>
"""
INSTALL_UPDATES_FAILED = """
    <body>
        <p>error installing updates</p>
    </body>
"""

def send_sendgrid_api_request(endpoint, payload):
    url = BASE_URL + endpoint
    settings = Settings()
    payload = json.loads(payload)
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.request(
        "POST",
        url,
        auth=(settings.master_username, settings.master_password),
        headers=headers,
        json=payload
    )

    return response

def install_webhook():
    return send_sendgrid_api_request("/webhooks", WEBHOOK_PAYLOAD)

def install_trigger_for_webhook(webhook_id):
    json_payload_as_string = TRIGGER_PAYLOAD % webhook_id

    return send_sendgrid_api_request("/triggers", json_payload_as_string)