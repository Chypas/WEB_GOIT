from json import loads
from mongoengine import disconnect

from models import Authors, Quotes


def seed_authors(file):
    json_file = file.read()
    data = loads(json_file)
    for authors in data:
        author = Authors(
            fullname=authors["fullname"],
            born_date=authors["born_date"],
            born_location=authors["born_location"],
            description=authors["description"],
        )
        author.save()


def seed_quotes(file):
    json_file = file.read()
    data = loads(json_file)
    for quotes in data:
        quote_author = Authors.objects(fullname=quotes["author"])
        quote = Quotes(
            tags=quotes["tags"], quote=quotes["quote"], author=quote_author[0]
        )
        quote.save()


if __name__ == "__main__":
    with open("authors.json", "r") as file:
        seed_authors(file)
    with open("quotes.json", "r") as file:
        seed_quotes(file)
    disconnect()
