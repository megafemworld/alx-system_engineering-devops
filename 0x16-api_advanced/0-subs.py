#!/usr/bin/python3
""" Reddit API"""
import json
import requests


def number_of_subscribers(subreddit):
    """return number of subscribers"""

    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'user-agent': 'megafemgroup API request for ALX'}
    client = requests.session()
    client.headers = headers
    response = client.get(api_url, allow_redirects=False)
    data = response.json()
    if response.status_code != 200:
        return 0
    sub_t = data.get("data").get("subscribers")
    return (sub_t)
