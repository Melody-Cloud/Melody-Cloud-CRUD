from playhouse.shortcuts import model_to_dict


def song_join_to_json(joined_object):
    song_json = model_to_dict(joined_object)

    song_json['id'] = joined_object.id

    song_json['artist'] = song_json['artistId']
    song_json['artistId'] = joined_object.artistId.id

    song_json['album'] = song_json['albumId']
    song_json['albumId'] = joined_object.albumId.id

    comments = list(joined_object.comments)
    song_json['comments'] = [model_to_dict(comment) for comment in comments]

    tags = list(joined_object.tags)
    song_json['tags'] = [model_to_dict(tag) for tag in tags]

    song_json['artist'] = model_to_dict(joined_object.artistId)
    return song_json
