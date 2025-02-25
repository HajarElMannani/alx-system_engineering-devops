#!/usr/bin/python3
'''queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit'''
import requests


def top_ten(subreddit):
    '''Print the titles of the first 10 hot posts listed for a given subreddit'''
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json?limit=10'
    headers = {'User-Agent': 'ALX-Project/1.0 by (u/Suspicious_Target472)'}
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code == 200:
        for child in data['children']:
            print(child.title)
    else:
        print(None)
