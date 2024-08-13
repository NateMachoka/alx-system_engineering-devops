#!/usr/bin/python3
"""
A script that queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords.
"""
import requests
import re


def count_words(subreddit, word_list, after=None, keyword_counts=None):
    """Recursively queries Reddit API to count keywords in hot article titles"""
    if keyword_counts is None:
        keyword_counts = {word.lower(): 0 for word in word_list}

    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'python:subreddit.hot.posts:v1.0 '
               '(by /u/SyllabubRealistic998)'}
    params = {'limit': 100, 'after': after}

    response = requests.get(
        URL, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code == 404:
        return None
    if response.status_code != 200:
        return

    try:
        results = response.json().get('data', {}).get('children', [])
        after = response.json().get('data', {}).get('after')
        if not results:
            return
        for post in results:
            title = post.get('data', {}).get('title', "").lower()
            for word in keyword_counts:
                keyword_pattern = r'\b{}\b'.format(re.escape(word))
                keyword_counts[word] += len(re.findall(keyword_pattern, title))
        # Continue with the next page if `after` is available
        if after:
            count_words(subreddit, word_list, after, keyword_counts)
    except ValueError:
        return

    if keyword_counts:
        sorted_counts = sorted(
            ((word, count) for word, count in keyword_counts.items() if count > 0),
            key=lambda x: (-x[1], x[0])
        )
        for word, count in sorted_counts:
            print(f"{word}: {count}")
