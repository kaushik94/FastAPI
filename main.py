import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

@app.get('/sidebar', response_class=HTMLResponse)
async def send_iframe_html():
    return """
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
        <p>Result: </p>
        </body>
        </html>
    """

@app.post('/install_update')
async def send_install_updates():
    os.system("bash create_sendesk_webhook.sh")
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Sample Form</title>
        </head>
        <body>
            <p>updates installed</p>
        </body>
        </html>
    """

@app.post('/webhook')
async def webhook():
    print("Hey there message received")