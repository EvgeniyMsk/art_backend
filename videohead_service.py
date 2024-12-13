import requests


def get_token() -> str:
    url = 'https://api.videohead.tech/api/lk/auth/token/'
    payload = {"login": "Pub 115951", "password": "115951"}
    return requests.post(url, json=payload).json()['token']


def get_stat():
    url = 'https://api.videohead.tech/api/lk/statistics/?start=2024-11-13&end=2024-12-13&group=host&limit=5'
    headers = {"Content-Type": "application/json; charset=utf-8", 'Authorization': 'Token ' + get_token()}
    return requests.get(url, headers=headers).json()


print(get_stat())