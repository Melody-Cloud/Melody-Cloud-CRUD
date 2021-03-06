from main import rest_app


def test_getting_albums():
    with rest_app.test_client() as c:
        rv = c.get('/api/album/')
        json_data = rv.get_json()
        assert json_data["meta"]["model"] == "album"
        assert "objects" in json_data


def test_getting_artist():
    with rest_app.test_client() as c:
        rv = c.get('/api/artist/')
        json_data = rv.get_json()
        assert json_data["meta"]["model"] == "artist"
        assert "objects" in json_data


def test_getting_comment():
    with rest_app.test_client() as c:
        rv = c.get('/api/comment/')
        json_data = rv.get_json()
        assert json_data["meta"]["model"] == "comment"
        assert "objects" in json_data


def test_getting_playlists():
    with rest_app.test_client() as c:
        rv = c.get('/api/playlists/')
        json_data = rv.get_json()
        assert "objects" in json_data


def test_getting_song():
    with rest_app.test_client() as c:
        rv = c.get('/api/song/')
        json_data = rv.get_json()
        assert json_data["meta"]["model"] == "song"
        assert "objects" in json_data


def test_getting_tag():
    with rest_app.test_client() as c:
        rv = c.get('/api/tag/')
        json_data = rv.get_json()
        assert json_data["meta"]["model"] == "tag"
        assert "objects" in json_data


# --- TEST POST METHOD ---

def test_adding_artist():
    with rest_app.test_client() as c:
        artist_to_add = {
          "name": "Test artist",
          "artistDescription": "This is test artist",
          "createdDate": "2018-12-05 18:02:10",
          "artistImageUrl": "https://instagram.fktw1-1.fna.fbcdn.net/vp/df0702bb3af8c1581864b98427644d8c/5C8E65A0/t51"
                            ".2885-15/e35/s320x320/26186297_1144045615726747_3534440781014106112_n.jpg "
        }

        rv = c.post('/api/artist/', json=artist_to_add)
        assert rv.status_code == 200

        artists_from_api = c.get('/api/artist/').get_json()["objects"]

        has_artist_been_added = any(
            [all(single_artist_from_api[key] == artist_to_add[key]
                 for key in artist_to_add.keys()) for single_artist_from_api in artists_from_api]
        )

        assert has_artist_been_added


def test_adding_album():
    with rest_app.test_client() as c:
        album_to_add = {
          "artistId": 1,
          "albumName": "TestAlb",
          "albumDescription": "Test desc",
          "createdDate": "2018-12-05 18:02:10"
        }

        rv = c.post('/api/album/', json=album_to_add)
        assert rv.status_code == 200

        albums_from_api = c.get('/api/album/').get_json()["objects"]

        has_album_been_added = any(
            [all(single_album_from_api[key] == album_to_add[key]
                 for key in album_to_add.keys()) for single_album_from_api in albums_from_api]
        )

        assert has_album_been_added


def test_adding_song():
    with rest_app.test_client() as c:
        song_to_add = {
          "artistId": 1,
          "albumId": 1,
          "name": "Test Song",
          "musicSrc": "https://s3-eu-west-1.amazonaws.com/melody-cloud-songs/Crybaby.mp3",
          "waveformImgUrl": "https://s3-eu-west-1.amazonaws.com/melody-cloud-waveforms/Crybaby.mp3.png",
          "amountOfPlays": 1,
          "amountOfLikes": 1,
          "description": "Test description",
          "lyrics": "Test lyrics",
          "createdDate": "2018-12-05 18:02:10"
        }

        rv = c.post('/api/song/', json=song_to_add)
        assert rv.status_code == 200

        songs_from_api = c.get('/api/song/').get_json()["objects"]

        has_song_been_added = any(
            [all(single_song_from_api[key] == song_to_add[key]
                 for key in song_to_add.keys()) for single_song_from_api in songs_from_api]
        )

        assert has_song_been_added


def test_adding_comment():
    with rest_app.test_client() as c:
        comment_to_add = {
          "songId": 1,
          "commentContent": "Test comment",
          "commentAuthorName": "Test comment author",
          "createdDate": "2018-12-05 18:02:12"
        }

        rv = c.post('/api/comment/', json=comment_to_add)
        assert rv.status_code == 200

        comments_from_api = c.get('/api/comment/').get_json()["objects"]

        has_comment_been_added = any(
            [all(single_comment_from_api[key] == comment_to_add[key]
                 for key in comment_to_add.keys()) for single_comment_from_api in comments_from_api]
        )

        assert has_comment_been_added


def test_adding_tag():
    with rest_app.test_client() as c:
        tag_to_add = {
            "songId": 4,
            "songTag": "Pop"
        }

        rv = c.post('/api/tag/', json=tag_to_add)
        assert rv.status_code == 200

        tags_from_api = c.get('/api/tag/').get_json()["objects"]
        assert tag_to_add in tags_from_api


def test_adding_playlist():
    with rest_app.test_client() as c:
        playlist_to_add = {
          "playlistName": "Test playlist",
          "songId": 1
        }

        rv = c.post('/api/playlist/', json=playlist_to_add)
        assert rv.status_code == 200

        playlists_from_api = c.get('/api/playlist/').get_json()["objects"]
        assert playlist_to_add in playlists_from_api
