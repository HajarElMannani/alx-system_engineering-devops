#!/usr/bin/python3
'''queries the Reddit API and returns a list containing the
 titles of all hot articles for a given subreddit recursively'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit'''
    hot_l = []
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    headers = {'User-Agent': 'ALX-Project/1.0 by (u/Suspicious_Target472)'}
    resp = requests.get(url, headers=headers, allow_redirects=False)
    data = response.json().get('data', {})
    children = data.get('children', [])
    for post in children:
        hot_l.append(post['data']['title'])
        after = data.get('after')
        if after is not None:
            return recurse(subreddit, hot_l, after)
        return hot_l
    else:
        return None
