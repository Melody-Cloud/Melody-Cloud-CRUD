from flask import Flask
from flask_peewee.rest import RestAPI
import psycopg2

from models import Message

app = Flask(__name__)

api = RestAPI(app)

# register our models so they are exposed via /api/<model>/
api.register(Message)

# configure the urls
api.setup()

rest_app = api.app


@rest_app.route('/')
def index():
    return "Hello, world!", 200


@rest_app.route('/hello')
def indexx():
    return "Hello, world!", 200


# We only need this for local development.
if __name__ == '__main__':
    app.run()
