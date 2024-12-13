from datetime import date

import requests
import datetime

from requests.cookies import RequestsCookieJar


def get_cookies() -> RequestsCookieJar:
    url_1 = 'https://api.buzzoola.com/v3/pub/publisher/login'
    data_1 = {
        "email": "san4ovilla@yandex.ru",
        "password": "moneymakers2018"
    }
    return requests.post(url_1, json=data_1).cookies


def get_stats(days: int) -> dict:
    url = 'https://api.buzzoola.com/v3/pub/publisher/stats'
    data = {"start": str(get_start(days)), "end": str(get_finish()), "placements": [], "period": "day"}
    print(data)
    return requests.post(url, json=data, cookies=get_cookies()).json()


def get_income() -> dict:
    url = 'https://api.buzzoola.com/v3/pub/publisher/stats/period-income'
    today_income = requests.get(url, cookies=get_cookies())
    return today_income.json()


def get_finish() -> date:
    return datetime.date.today() + datetime.timedelta(days=1)


def get_start(days: int) -> date:
    return get_finish() - datetime.timedelta(days=days)


def get_total_pub_paid_events(days: int):
    result_data = get_stats(days)['result']['data']
    result = 0
    for data in result_data:
        result += float(data['data']['pub_paid_events'])
    return result


def get_total_cpm(days: int):
    result_data = get_stats(days)['result']['data']
    result = 0
    for data in result_data:
        result += float(data['data']['cpm'])
    return result / len(result_data)


def get_total_revenue(days: int):
    result_data = get_stats(days)['result']['data']
    result = 0
    for data in result_data:
        result += float(data['data']['revenue'])
    return result
