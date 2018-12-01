from flask import Flask
from flask import request
from flask import send_file

import requests

app = Flask(__name__)
key = ''

@app.route('/callback', methods=['POST','GET'])
def _callback():
    return ''

@app.route('/mlh/emomap/tag/<tag>', methods=['POST'])
def _tag(tag):
    return tag

def query(tag):
    url = 'https://api.twitter.com/1.1/tweets/search/7day/Prod.json'
    headers = {'authorization':'Bearer 1068901758318067712-rWTsS7K8CFeMTgT7JT4IQe9UbA2zic'}
    data = {'query':'from:JimWatsonOttawa lang:en', 'maxResults':16, 'fromDate':

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969)
