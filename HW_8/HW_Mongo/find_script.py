import redis
from redis_lru import RedisLRU
from mongoengine import DoesNotExist

from models import Authors, Quotes


client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def find_quote_by_name(value):
    try:
        author = Authors.objects(fullname__startswith=value.title())[0]
        quotes = Quotes.objects(author=author)
        if quotes:
            result = []
            for quote in quotes:
                r = f"{quote.quote}\n{quote.author.fullname}     tags:{', '.join(quote.tags)}"
                result.append(r)
            return result
    except DoesNotExist:
        print(f"Quotes by {value} is not exists")


@cache
def find_quote_by_tag(value):
    try:
        result = []
        for quote in Quotes.objects(tags__startswith=value):
            r = f"{quote.quote}\n{quote.author.fullname}     tags: {', '.join(quote.tags)}"
            result.append(r)
        return result
    except DoesNotExist:
        print(f"Quotes with tag:{value} is not exists")


@cache
def find_quote_by_tags(value):
    try:
        result = []
        for quote in Quotes.objects():
            for tag in quote.tags:
                if tag in value.split(","):
                    r = f"{quote.quote}\n{quote.author.fullname}      tags: {', '.join(quote.tags)}"
                    if r not in result:
                        result.append(r)
        return result
    except DoesNotExist:
        print(f"Quotes with tag:{value} is not exists")


def main():
    while True:
        user_command = input("Enter command: ").strip().lower()
        if user_command == "exit":
            print("Good bye!")
            break
        else:
            try:
                command, value = user_command.split(":")
                command, value = command.strip(), value.strip()

                if command == "name":
                    print(*find_quote_by_name(value), sep="\n")

                elif command == "tag":
                    print(*find_quote_by_tag(value), sep="\n")

                elif command == "tags":
                    print(*find_quote_by_tags(value), sep="\n")
                else:
                    print("Wrong command. Try again!")
            except Exception as err:
                print(err)


if __name__ == "__main__":
    main()
