from mongoengine import *

connect(host="mongodb+srv://chypa:Chypa1990@goitdb.ewrnrcn.mongodb.net/test")


class Authors(Document):
    fullname = StringField(max_length=100, required=True)
    date_born = StringField(max_length=100)
    born_location = StringField(max_length=100)
    bio = StringField()


class Quotes(Document):
    tags = ListField(StringField(max_length=100))
    author = ReferenceField(Authors, reverse_delete_rule=CASCADE)
    quote = StringField()
    meta = {"allow_inheritance": True}
