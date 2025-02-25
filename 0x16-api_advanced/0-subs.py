#!/usr/bin/python3
'''function that returns the number of all subscribers of Reddit APIfor a given subreddit '''
import requests


def number_of_subscribers(subreddit):
    '''returns the number of all subscribers of Reddit\
     APIfor a given subreddit '''
    headers = {'User-Agent': 'MyRedditBot/1.0 (by /u/Suspicious_Target472)'}
    resp = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit), headers=headers, allow_redirects=False)
    print(resp.status_code) 
    if resp.status_code == 200:
        response = resp.json()
        return response['data'].get('subscribers')

    else:
        return 0
