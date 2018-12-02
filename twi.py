import requests
import urllib
import base64

consumer_key = 'rDOI6D4qdYOfZVLIYCD717Sqp'
consumer_secret = 'TsTBkDNRh1HJXbURhEu4Qxy9tDywinIAStmhWuwXfA9SBsOyaV'

ckey_url = urllib.parse.quote_plus(consumer_key)
csec_url = urllib.parse.quote_plus(consumer_secret)
credentials = base64.b64encode('{}:{}'.format(ckey_url, csec_url).encode()).decode('ascii')

def authorize():
    headers = {'Authorization': 'Basic {}'.format(credentials)}
    data = {'grant_type':'client_credentials'}
    r = requests.post('https://api.twitter.com/oauth2/token', headers=headers, data=data)
    
    if r.status_code == 200:
        print('Token Generated')
        return r.json()['access_token']
    print(r.status_code)
    print(r.text)
    return None

def invalidate(token):
    if token == None:
        return None
    print(token)
    headers = {'Authorization': 'Basic {}'.format(credentials)}
    data = {'access_token': token}
    r = requests.post('https://api.twitter.com/oauth2/invalidate_token', headers=headers, data=data)
    print(r.status_code)

def search(token, query_string):
    headers = {'Authorization': 'Bearer {}'.format(token)}
    query = urllib.parse.quote_plus(query_string)
    r = requests.get('https://api.twitter.com/1.1/search/tweets.json?l=en&q={}&count=10'.format(query), headers=headers)
    
    if r.status_code == 200:
        return r.text
    return '[]'
