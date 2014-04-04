from flask_peewee.rest import RestAPI, UserAuthentication

from app import app
from auth import auth
from models import Note

user_auth = UserAuthentication(auth)
api = RestAPI(app, default_auth=user_auth)
api.register(Note)
api.setup()
