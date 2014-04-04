from flask_peewee.admin import Admin, ModelAdmin

from app import app
from auth import auth
from models import Note


class NoteAdmin(ModelAdmin):
    columns = ('message', 'created',)

admin = Admin(app, auth)
admin.register(Note, NoteAdmin)
auth.register_admin(admin)
admin.setup()

