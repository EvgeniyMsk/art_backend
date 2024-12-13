from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import buzzoola_service as buzz_svc
import videohead_service as video_svc

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={
            "buzzoola_income": buzz_svc.get_income(),
            "buzzoola_stats": buzz_svc.get_stats(),
            "videohead_stats": video_svc.get_stat()
        }
    )


@app.get("/buzzoola/income")
async def buzzoola_income():
    return buzz_svc.get_income()


@app.get("/buzzoola/stats")
async def buzzoola_stats():
    return buzz_svc.get_stats()


@app.get("/videohead/stats")
async def videohead_stats():
    return video_svc.get_stat()


