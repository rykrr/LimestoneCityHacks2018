from flask import Flask

app = Flask(__name__)

@app.route('/callback', methods=['POST','GET'])
def _callback():
    return ''

@app.route('/mlh/emomap/tag/<tag>', methods=['POST'])
def _tag(tag):
    return tag

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969)
