from tortoise.models import Model
from tortoise.fields import IntField, CharField, TextField


class Todo(Model):
    id = IntField(pk=True)
    title = CharField(max_length=100, null=False)
    description = TextField(null=False)
