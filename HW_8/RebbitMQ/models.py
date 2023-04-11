from mongoengine import *

connect(host="mongodb+srv://chypa:Chypa1990@goitdb.ewrnrcn.mongodb.net/contacts")


class Contacts(Document):
    fullname = StringField(max_length=80, required=True)
    email = StringField(max_length=50)
    number = StringField(max_length=50)
    send = BooleanField(default=False)

