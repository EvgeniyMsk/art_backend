from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import datetime

import buzzoola_service as buzz_svc
import videohead_service as video_svc

app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={
            "buzzoola_income": buzz_svc.get_income(),
            "buzzoola_stats_1": buzz_svc.get_stats(1),
            "buzzoola_stats_5": buzz_svc.get_stats(datetime.date.today().weekday() + 1),
            "buzzoola_stats_30": buzz_svc.get_stats(datetime.date.today().day),

            "total_pub_paid_events_1": buzz_svc.get_total_pub_paid_events(1),
            "total_pub_paid_events_5": buzz_svc.get_total_pub_paid_events(datetime.date.today().weekday() + 1),
            "total_pub_paid_events_30": buzz_svc.get_total_pub_paid_events(datetime.date.today().day),

            "total_cpm_1": buzz_svc.get_total_cpm(1),
            "total_cpm_5": buzz_svc.get_total_cpm(datetime.date.today().weekday() + 1),
            "total_cpm_30": buzz_svc.get_total_cpm(datetime.date.today().day),

            "total_revenue_1": buzz_svc.get_total_revenue(1),
            "total_revenue_5": buzz_svc.get_total_revenue(datetime.date.today().weekday() + 1),
            "total_revenue_30": buzz_svc.get_total_revenue(datetime.date.today().day),

            "earnings_1": video_svc.get_earnings(1),
            "earnings_5": video_svc.get_earnings(datetime.date.today().weekday() + 1),
            "earnings_30": video_svc.get_earnings(datetime.date.today().day),

            "videohead_stats_1": video_svc.get_stat(1),
            "videohead_stats_5": video_svc.get_stat(datetime.date.today().weekday() + 1),
            "videohead_stats_30": video_svc.get_stat(datetime.date.today().day),
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



