import requests


def get_task():
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    return response.json()


def my_daily_to_do():
    return [get_task()]

