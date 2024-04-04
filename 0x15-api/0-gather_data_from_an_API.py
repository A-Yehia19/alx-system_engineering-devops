#!/usr/bin/python3
'''gather data from API'''

import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    user_id = sys.argv[1]
    user = requests.get(REST_API + "/users/{}".format(user_id)).json()
    tasks = requests.get(REST_API + "/todos?userId={}".format(user_id)).json()

    completed_tasks = [task for task in tasks if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(tasks)))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
