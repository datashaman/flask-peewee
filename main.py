from app import app
from models import Note

from auth import auth
from admin import admin
from api import api

if __name__ == '__main__':
    auth.User.create_table(fail_silently=True)
    Note.create_table(fail_silently=True)
    app.run()
