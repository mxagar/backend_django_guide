from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def endpoint_1():
    return "<h2>This is the response coming from Backend-Server-1: endpoint-1</h2>"


@app.get("/test", response_class=HTMLResponse)
def endpoint_2():
    return "<h2>This is the response coming from Backend-Server-1: endpoint-2</h2>"
