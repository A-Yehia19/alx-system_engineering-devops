#!/usr/bin/python3
'''gather data from API'''

import requests


def top_ten(subreddit):
    '''get top ten posts from subreddit'''
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        for post in response.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)
