#!/usr/bin/python3
"""A script that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit."""
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"  # Replace with your username
    }
    params = {
        "limit": 10
    }

    response = requests.get(
        URL, headers=headers, params=params, allow_redirects=False
    )
    
    # Debugging: Print the status code and response text
    print("Status Code:", response.status_code)

    if response.status_code != 200:
        print(None)
        return
    
    try:
        data = response.json()
        print("Response JSON Data:", data)  # Debugging: Print the entire JSON response
        results = data.get('data', {}).get('children', [])
        
        if not results:
            print(None)
            return
        
        for post in results:
            print(post.get('data', {}).get('title', 'No Title'))
    except Exception as e:
        print("Error:", e)
        print(None)
