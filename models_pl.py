import datetime

from peewee import TextField, DateTimeField, Model, CharField, ForeignKeyField, IntegerField

from persistence import pgdb


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = pgdb


class Artysta(BaseModel):
    nazwa = CharField()
    opis = TextField()
    data_utworzenia = DateTimeField(default=datetime.datetime.now)
    zdjecie = TextField()


class Album(BaseModel):
    artysta = ForeignKeyField(Artysta, backref='albums')
    tytul = CharField()
    opis = TextField()
    okladka = TextField()
    data_utworzenia = DateTimeField(default=datetime.datetime.now)


class Utwor(BaseModel):
    artysta = ForeignKeyField(Artysta, backref='songs')
    album = ForeignKeyField(Album, backref='tags')
    tytul = CharField()
    # zrodlo = CharField() ? moze niepotrzebne
    waveform = TextField()
    liczba_odtworzen = IntegerField()
    liczba_polubien = IntegerField()
    opis = TextField()
    tekst = TextField()
    data_utworzenia = DateTimeField(default=datetime.datetime.now)


class Tag(BaseModel):
    utwor = ForeignKeyField(Utwor, backref='tags')
    nazwa_taga = CharField()

    class Meta:
        primary_key = False


class Komentarz(BaseModel):
    utwor = ForeignKeyField(Utwor, backref='comments')
    tresc = TextField()
    nazwa_autora = CharField()
    data_utworzenia = DateTimeField(default=datetime.datetime.now)


class ListaOdtwarzania(BaseModel):
    nazwa = CharField()
    utwor = ForeignKeyField(Utwor, backref='songs')

    class Meta:
        primary_key = False


# pgdb.create_tables([Utwor])
# pgdb.create_tables([Tag])
# pgdb.create_tables([Komentarz])
# pgdb.create_tables([Artysta])
# pgdb.create_tables([Album])
# pgdb.create_tables([ListaOdtwarzania])

pgdb.create_tables([Utwor, Tag, Komentarz, Artysta, Album, ListaOdtwarzania])
# pgdb.create_tables([Tag])
