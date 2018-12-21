from flask import Flask, jsonify
from flask_cors import CORS

from flask_peewee.rest import RestAPI
import psycopg2

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from helpers import song_join_to_json
from models import Song, Artist, Comment, Album, Playlist, Tag
from no_auth import NoAuth

user_auth = NoAuth()

models_to_register = [Song, Tag, Comment, Artist, Album, Playlist]

app = Flask(__name__)
api = RestAPI(app, default_auth=user_auth)

# register our models so they are exposed via /api/<model>/
for model_to_register in models_to_register:
    api.register(model_to_register)

# configure the urls
api.setup()

rest_app = api.app

# configure limiter in order to prevent abuse
limiter = Limiter(
    rest_app,
    key_func=get_remote_address,
    default_limits=["50 per second"]
)


@rest_app.route('/')
def index():
    return "Hello, world!", 200


@rest_app.route('/api/hello')
def indexx():
    return "Hello, world!", 200


@rest_app.route('/api/playlists/')
def playlists():
    distinct_list = Playlist.select(Playlist.playlistName).distinct().execute()

    return jsonify({"objects": [playlist.playlistName for playlist in distinct_list]})


@rest_app.route('/api/songs-feed/')
def songs():
    query = Song.select()

    query_results = list(query)
    results = [song_join_to_json(result) for result in query_results]

    return jsonify({"objects": results})


cors = CORS(rest_app)
rest_app.config['CORS_HEADERS'] = 'Content-Type'


# We only need this for local development.
if __name__ == '__main__':
    rest_app.run()
