import datetime

from peewee import TextField, DateTimeField, Model, CharField, ForeignKeyField, IntegerField

from persistence import pgdb


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = pgdb


class Artist(BaseModel):
    name = CharField()
    artistDescription = TextField()
    createdDate = DateTimeField(default=datetime.datetime.now)
    artistImageUrl = CharField()


class Album(BaseModel):
    artistId = ForeignKeyField(Artist, backref='albums')
    albumName = CharField()
    albumDescription = TextField()
    createdDate = DateTimeField(default=datetime.datetime.now)


class Song(BaseModel):
    artistId = ForeignKeyField(Artist, backref='songs')
    albumId = ForeignKeyField(Album, backref='tags')
    name = CharField()
    musicSrc = CharField()
    waveformImgUrl = CharField()
    amountOfPlays = IntegerField()
    amountOfLikes = IntegerField()
    description = TextField()
    lyrics = TextField()
    createdDate = DateTimeField(default=datetime.datetime.now)


class Tag(BaseModel):
    songId = ForeignKeyField(Song, backref='tags')
    songTag = CharField()

    class Meta:
        primary_key = False


class Comment(BaseModel):
    songId = ForeignKeyField(Song, backref='comments')
    commentContent = TextField()
    commentAuthorName = CharField()
    createdDate = DateTimeField(default=datetime.datetime.now)


class Playlist(BaseModel):
    playlistName = CharField()
    songId = ForeignKeyField(Song, backref='songs')

    class Meta:
        primary_key = False


pgdb.create_tables([Song, Tag, Comment, Artist, Album, Playlist])
# pgdb.create_tables([Tag])
