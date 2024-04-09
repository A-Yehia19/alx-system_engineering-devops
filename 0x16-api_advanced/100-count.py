#!/usr/bin/python3
'''gather data from API'''

import requests


def count_words(subreddit, word_list, word_count={}, count=0, after=""):
    '''get sorted list of hot posts from subreddit'''

    # initialize word_count dictionary with word_list
    if not word_count:
        for word in word_list:
            if word.lower() not in word_count:
                word_count[word.lower()] = 0

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
            title = post.get("data").get("title").lower().split()
            for word in word_list:
                word_count[word.lower()] += title.count(word.lower())

        if after is not None:
            count_words(subreddit, word_list, word_count, count, after)

        # print the sorted key words
        else:
            final_words = sorted(word_count.items(), key=lambda x: x[1],
                                 reverse=True)
            for key, value in final_words:
                if value > 0:
                    print("{}: {}".format(key, value))
