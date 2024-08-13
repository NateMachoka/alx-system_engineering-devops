#!/usr/bin/python3
"""
This module defines a function to query the Reddit API and return the number of
subscribers.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and gives the number of subscribers for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': ('python:subreddit.subscriber.count:v1.0 '
                   '(by /u/yourusername)')
        }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        elif response.status_code in [301, 302, 404]:
            # Handle redirection or not found
            return 0
        else:
            # Any other unexpected status codes
            return 0
    except requests.RequestException as e:
        return 0
