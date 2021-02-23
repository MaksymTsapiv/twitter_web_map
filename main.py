from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Random phrase")
templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
async def read_items():
    return templates.TemplateResponse("index.html", {})


