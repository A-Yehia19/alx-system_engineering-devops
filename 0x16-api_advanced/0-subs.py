#!/usr/bin/python3
'''gather data from API'''

import requests


def number_of_subscribers(subreddit):
    '''get number of subscribers'''
    url = "https://www.reddit.com/r/{}/about/.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0

import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))