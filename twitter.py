import requests
import urllib
import base64

consumer_key = 'rDOI6D4qdYOfZVLIYCD717Sqp'
consumer_secret = ''

ckey_url = urllib.parse.quote_plus(consumer_key)
csec_url = urllib.parse.quote_plus(consumer_secret)
credentials = base64.b64encode('{}:{}'.format(ckey_url, csec_url).encode()).decode('ascii')

def authorize():
    headers = {'Authorization': 'Basic {}'.format(credentials)}
    data = {'grant_type':'client_credentials'}
    r = requests.post('https://api.twitter.com/oauth2/token', headers=headers, data=data)

    if r.status_code == 200:
        return r.json()['access_token']
    return None

def invalidate(token):
    if token == None:
        return None
    print(token)
    headers = {'Authorization': 'Basic {}'.format(credentials)}
    data = {'access_token': token}
    r = requests.post('https://api.twitter.com/oauth2/invalidate_token', headers=headers, data=data)
    print(r.status_code)

token = authorize();
invalidate(token);
