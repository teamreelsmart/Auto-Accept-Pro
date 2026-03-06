from os import environ
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Bot is running'


if __name__ == "__main__":
    port = int(environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
