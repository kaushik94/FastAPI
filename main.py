from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

@app.get('/sidebar')
def send_iframe_html():
    return '<p>App content from the server</p>'