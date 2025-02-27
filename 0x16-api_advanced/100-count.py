#!/usr/bin/python3
'''Query the Reddit API, parses the title of all hot articles,
 and prints a sorted count of given keywords'''
import requests


def count_words(subreddit, word_list, word_count=None, after=None):
    '''Query the Reddit API, parses the title of all hot articles,
 and prints a sorted count of given keywords'''
    if word_count is None:
        word_count = {}
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    headers = {'User-Agent': 'ALX-Project/1.0 by (u/Suspicious_Target472)'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers,
                            params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json().get('data', {})
    children = data.get('children', [])
    normalized_words = [word.lower() for word in word_list]
    for post in children:
        title = post['data']['title'].lower().split()
        for word in normalized_words:
            word_count[word] = word_count.get(word, 0) + title.count(word)
    after = data.get('after')
    if after is not None:
        return count_words(subreddit, word_list, word_count, after)
    sorted_words = sorted(
        [(word, count) for word, count in word_count.items() if count > 0],
        key=lambda u: (-u[1], u[0])
    )
    for word, count in sorted_words:
        print("{}: {}".format(word, count))
