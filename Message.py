from datetime import *
from peewee import *

db = MySQLDatabase('Chat',user='root',passwd='')

class Message(Model):
    name = CharField(null=False,max_length=30)
    date = DateTimeField(null=False,default=datetime.now())
    text_message = CharField(null=False)

    class Meta:
        database = db

    def __str__(self):
        return self.name + ': ' + self.text_message