from datetime import date

import requests
import datetime


def get_token() -> str:
    url = 'https://api.videohead.tech/api/lk/auth/token/'
    payload = {"login": "Pub 115951", "password": "115951"}
    return requests.post(url, json=payload).json()['token']


def get_stat(days: int) -> str:
    url = 'https://api.videohead.tech/api/lk/statistics/?start=' + str(get_start(days)) + '&end=' + str(get_finish()) + '&group=host'
    headers = {"Content-Type": "application/json; charset=utf-8", 'Authorization': 'Token ' + get_token()}
    return requests.get(url, headers=headers).json()


def get_earnings(days: int) -> str:
    url = 'https://api.videohead.tech/api/lk/earnings/?start=' + str(get_start(days)) + '&end=' + str(get_finish()) + '&group=host'
    headers = {"Content-Type": "application/json; charset=utf-8", 'Authorization': 'Token ' + get_token()}
    return requests.get(url, headers=headers).json()


def get_finish() -> date:
    return datetime.date.today() + datetime.timedelta(days=1)


def get_start(days: int) -> date:
    return get_finish() - datetime.timedelta(days=days)

