import datetime

from peewee import TextField, DateTimeField, Model, CharField, ForeignKeyField, IntegerField

from persistence_configuration import pgdb


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = pgdb


class Artist(BaseModel):
    name = CharField()
    artistDescription = TextField(null=True)
    createdDate = DateTimeField(default=datetime.datetime.now)
    artistImageUrl = CharField(null=True)


class Album(BaseModel):
    artistId = ForeignKeyField(Artist, backref='albums')
    albumName = CharField()
    albumDescription = TextField(null=True)
    createdDate = DateTimeField(default=datetime.datetime.now)


class Song(BaseModel):
    artistId = ForeignKeyField(Artist, backref='songs')
    albumId = ForeignKeyField(Album, backref='tags', null=True)
    name = CharField()
    musicSrc = CharField()
    waveformImgUrl = CharField(null=True)
    amountOfPlays = IntegerField(null=True)
    amountOfLikes = IntegerField(null=True)
    description = TextField(null=True)
    lyrics = TextField(null=True)
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
