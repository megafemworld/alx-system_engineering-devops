#!/usr/bin/python3
""" Reddit API"""
import requests, json

def number_of_subscribers(subreddit):
    """return number of subscribers"""

    api_url = f"https://api.reddit.com/r/{subreddit}/about.json"
    response = requests.get(api_url)
    data = response.json()
    if response.status_code != 200:
        return 0
    sub_t = data.get("data").get("subscribers")
    return (sub_t)
