#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    # Set the URL for the subreddit about.json endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'custom-script/1.0'}
    
    try:
        # Make the request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # If the status code is not 200, return 0
            return 0
    except requests.RequestException:
        # If there's an exception (e.g., network error), return 0
        return 0

