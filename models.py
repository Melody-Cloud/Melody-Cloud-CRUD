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


class Album(BaseModel):
    artistId = ForeignKeyField(Artist, backref='albums')
    albumName = CharField()
    albumDescription = TextField()
    createdDate = DateTimeField(default=datetime.datetime.now)


class Song(BaseModel):
    artistId = ForeignKeyField(Artist, backref='songs')
    albumId = ForeignKeyField(Album, backref='tags')
    name = CharField()
    musicSrcUrl = CharField()
    waveformImgUrl = CharField()
    amountOfPlays = IntegerField()
    amountOfLike = IntegerField()
    description = TextField()
    createdDate = DateTimeField(default=datetime.datetime.now)


class Tag(BaseModel):
    songId = ForeignKeyField(Song, backref='tags')
    songTag = CharField()
    createdDate = DateTimeField(default=datetime.datetime.now)


class Comment(BaseModel):
    songId = ForeignKeyField(Song, backref='comments')
    commentContent = TextField()
    createdDate = DateTimeField(default=datetime.datetime.now)


class Playlist(BaseModel):
    playlistName = CharField()
    songId = ForeignKeyField(Song, backref='songs')


pgdb.create_tables([Song, Tag, Comment, Artist, Album, Playlist])
