from flask import Flask
import flask
import twi
import wat
import json

app = Flask(__name__)

token = twi.authorize()


def analyze(data):
    output = []
    for d in data['statuses']:
        url = ''
        if len(d['entities']['urls']) != 0:
            url = d['entities']['urls'][0]['expanded_url']
        tweet = {'url': url, 'text': d['text'], 'tones': []}
        tweet['tones'] = wat.tone(tweet['text'])['document_tone']['tones']
        output.append(tweet)
    return output


@app.route('/callback', methods=['POST','GET'])
def _callback():
    return ''


@app.route('/test/query/<query>', methods=['GET'])
def _test_query(query):
    try:
        cache = open('cache/{}.json'.format(query), 'r').read()
        out = flask.make_response(cache)
        out.headers.add('Access-Control-Allow-Origin', '*')
        return out
    except Exception as e:
        print(e.message)
        return '[]'

@app.route('/query/<query>', methods=['GET'])
def _query(query):
    try:
        data = json.loads(twi.search(token, '%23{}'.format(query)))
        f = open('cache/{}.json'.format(query), 'w')
        
        result = analyze(data)
        
        cache = json.dumps(result)
        f.write(cache)
        
        out = flask.make_response(cache)
        out.headers.add('Access-Control-Allow-Origin', '*')
        return out
    except Exception as e:
        print(e.message)
        return '[]'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969)
