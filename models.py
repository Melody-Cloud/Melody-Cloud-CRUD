import datetime

from peewee import TextField, DateTimeField, Model

from persistence import pgdb


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = pgdb


class Message(BaseModel):
    content = TextField()
    pub_date = DateTimeField(default=datetime.datetime.now)


pgdb.create_tables([Message])
