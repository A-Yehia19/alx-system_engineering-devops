#!/usr/bin/python3
'''gather data from API'''

import requests


def top_ten(subreddit):
    '''get top ten posts from subreddit'''
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        posts = response.json().get("data").get("children")
        if len(posts) == 0:
            print(None)
        else:
            for post in posts:
                print(post.get("data").get("title"))
