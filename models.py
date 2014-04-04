import datetime

from flask_peewee.db import Database
from app import app
from peewee import TextField, DateTimeField


db = Database(app)

class Note(db.Model):
    message = TextField()
    created = DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.message
