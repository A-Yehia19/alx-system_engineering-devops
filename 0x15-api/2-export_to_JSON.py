#!/usr/bin/python3
'''gather data from API'''

import json
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    user_id = sys.argv[1]
    user = requests.get(REST_API + "/users/{}".format(user_id)).json()
    tasks = requests.get(REST_API + "/todos?userId={}".format(user_id)).json()

    data = {}
    data[user_id] = []
    for task in tasks:
        data[user_id].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        })

    with open('{}.json'.format(user_id), 'w') as file:
        json.dump(data, file)
