from flask import Flask, jsonify
from flask_peewee.rest import RestAPI
from flask_cors import CORS
import psycopg2

from models import Song, Artist, Comment, Album, Playlist, Tag

models_to_register = [Song, Tag, Comment, Artist, Album, Playlist]

app = Flask(__name__)
api = RestAPI(app)

# register our models so they are exposed via /api/<model>/
for model_to_register in models_to_register:
    api.register(model_to_register)

# configure the urls
api.setup()

rest_app = api.app


@rest_app.route('/')
def index():
    return "Hello, world!", 200


@rest_app.route('/api/hello')
def indexx():
    return "Hello, world!", 200


@rest_app.route('/api/playlists')
def playlists():
    distinct_list = Playlist.select(Playlist.playlistName).distinct().execute()

    return jsonify({"objects": [playlist.playlistName for playlist in distinct_list]})


cors = CORS(rest_app)
rest_app.config['CORS_HEADERS'] = 'Content-Type'


# We only need this for local development.
if __name__ == '__main__':
    rest_app.run()
