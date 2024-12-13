from datetime import date

import requests
import datetime


def get_token() -> str:
    url = 'https://api.videohead.tech/api/lk/auth/token/'
    payload = {"login": "Pub 115951", "password": "115951"}
    return requests.post(url, json=payload).json()['token']


def get_stat():
    url = 'https://api.videohead.tech/api/lk/statistics/?start=' + str(get_start()) + '&end=' + str(get_finish()) + '&group=host&limit=5'
    headers = {"Content-Type": "application/json; charset=utf-8", 'Authorization': 'Token ' + get_token()}
    return requests.get(url, headers=headers).json()


def get_finish() -> date:
    return datetime.date.today()


def get_start() -> date:
    return datetime.date.today() - datetime.timedelta(days=30)


print(get_stat())
