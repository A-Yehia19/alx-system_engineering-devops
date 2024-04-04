#!/usr/bin/python3
'''gather data from API'''

import requests
import sys
import json

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    users = requests.get(REST_API + "/users").json()
    data = {}
    for user in users:
        user_id = user.get("id")
        data[user_id] = []

        tasks = requests.get(REST_API + "/todos?userId={}".format(user_id))
        tasks = tasks.json()
        for task in tasks:
            data[user_id].append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            })

    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)
