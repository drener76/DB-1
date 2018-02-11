from model import *

class Event(Model):
    base = BooleanField(default=False)

    user = ForeignKeyField(User, null=True)
    world = ForeignKeyField(World, null=False)