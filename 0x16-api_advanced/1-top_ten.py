#!/usr/bin/python3
"""
A script that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'python:subreddit.hot.posts:v1.0 (by /u/SyllabubRealistic998)'
    }
    params = {'limit': 10}  # Limit to 10 posts

    response = requests.get(URL, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 404:
        print(None)
        return

    if response.status_code == 403:
        print("Access forbidden: Ensure User-Agent is correct and you are not rate-limited.")
        return
    
    if response.status_code == 200:
        try:
            results = response.json().get('data', {}).get('children', [])
            if not results:
                print(None)
                return
            for post in results:
                print(post.get('data', {}).get('title'))
        except ValueError:  # JSON decoding failed
            print(None)
    else:
        print(None)
