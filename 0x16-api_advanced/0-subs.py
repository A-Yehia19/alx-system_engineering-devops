#!/usr/bin/python3
'''gather data from API'''

import requests


def number_of_subscribers(subreddit):
    '''get number of subscribers'''
    url = "https://www.reddit.com/r/{}/about/.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    try:
        return response.json().get("data").get("subscribers")
    except Exception:
        return 0
