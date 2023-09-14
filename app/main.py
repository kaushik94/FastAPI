import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from app.dependencies import install_trigger_for_webhook, install_webhook, INSTALL_NEW_UPDATES_HTML, INSTALL_UPDATES_SUCCESSFUL, INSTALL_UPDATES_FAILED

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

@app.get('/sidebar', response_class=HTMLResponse)
async def send_iframe_html():
    return INSTALL_NEW_UPDATES_HTML

@app.post('/install_update', response_class=HTMLResponse)
async def send_install_updates():
    response = install_webhook()
    if (response.ok):
        res_json = response.json()
        webhook_id = res_json["webhook"]["id"]
        res = install_trigger_for_webhook(webhook_id)
        return INSTALL_UPDATES_SUCCESSFUL
    else:
        return INSTALL_UPDATES_FAILED

@app.post('/webhook')
async def webhook(
    request: Request
):
    print("Hey there message received", request)