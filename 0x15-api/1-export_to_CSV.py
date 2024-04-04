#!/usr/bin/python3
'''gather data from API'''

import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    user_id = sys.argv[1]
    user = requests.get(REST_API + "/users/{}".format(user_id)).json()
    tasks = requests.get(REST_API + "/todos?userId={}".format(user_id)).json()

    with open('{}.csv'.format(user_id), 'w') as file:
        username = user.get("username")
        for task in tasks:
            task_status = task.get("completed")
            task_title = task.get("title")
            file.write('"{}","{}","{}","{}"\n'.format(
                user_id, username, task_status, task_title))
