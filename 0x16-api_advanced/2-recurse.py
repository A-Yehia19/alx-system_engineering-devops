#!/usr/bin/python3
'''gather data from API'''

import requests


def recurse(subreddit, hot_list=[], count=0, after=""):
    '''get number of subscribers'''
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {
        "after": after,
        "count": count
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        result = response.json().get("data")
        after = result.get("after")
        count += result.get("dist")

        for post in result.get("children"):
            hot_list.append(post.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, count, after)

        return hot_list
    else:
        return None
