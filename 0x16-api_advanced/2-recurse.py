#!/usr/bin/python3
"""
A script that queries the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[]):
    """Recursively queries Reddit API and returns a list of all hot titles."""
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'python:subreddit.hot.posts:v1.0 '
               '(by /u/SyllabubRealistic998)'}
    params = {'limit': 100}

    response = requests.get(
        URL, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code == 404:
        return None
    if response.status_code == 200:
        try:
            data = response.json().get('data', {})
            children = data.get('children', [])
            if not children:
                return hot_list
            for post in children:
                hot_list.append(post.get('data', {}).get('title'))

            after = data.get('after')
            if after:
                # Recursive call to get the next page
                return recurse(subreddit, hot_list)
            else:
                return hot_list
        except ValueError:
            return None
    else:
        return None
