import requests
import json

_username = 'apikey'
_password = ''
_version  = '2017-09-21'

def tone(text):
    text = text.encode('utf-8')
    auth = (_username, _password)
    header = {'content-type': 'text/plain;charset=UTF-8'}
    
    r = requests.post('https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21', auth=auth, headers=header, data=text)
    #r = requests.post('http://localhost:8080', auth=auth, headers=header, data=text)
    
    if r.status_code == 200:
        return json.loads(r.text)
    print(r.status_code)
    return {'document_tone':{'tones':[]}}
