import datetime

import requests
from requests.cookies import RequestsCookieJar


def get_cookies() -> RequestsCookieJar:
    url_1 = 'https://api.buzzoola.com/v3/pub/publisher/login'
    data_1 = {
        "email": "san4ovilla@yandex.ru",
        "password": "moneymakers2018"
    }
    return requests.post(url_1, json=data_1).cookies


def get_stats():
    url_2 = 'https://api.buzzoola.com/v3/pub/publisher/stats'
    data_2 = {"start": str(datetime.date.today() - datetime.timedelta(days=7)), "end": str(datetime.date.today()), "placements": [], "period": "day"}
    return requests.post(url_2, json=data_2, cookies=get_cookies()).json()


def get_income():
    url_3 = 'https://api.buzzoola.com/v3/pub/publisher/stats/period-income'
    today_income = requests.get(url_3, cookies=get_cookies())
    return today_income.json()


def set_start():
    print(datetime.date.today() - datetime.timedelta(days=7))

set_start()
