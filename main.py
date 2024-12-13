from fastapi import FastAPI

import buzzoola_service as buzz_svc
import videohead_service as video_svc

app = FastAPI()


@app.get("/buzzoola/income")
async def buzzoola_income():
    return buzz_svc.get_income()


@app.get("/buzzoola/stats")
async def buzzoola_stats():
    return buzz_svc.get_stats()


@app.get("/videohead/stats")
async def buzzoola_stats():
    return video_svc.get_stat()
