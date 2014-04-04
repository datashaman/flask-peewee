from flask_peewee.auth import Auth

from app import app
from models import db


auth = Auth(app, db)
