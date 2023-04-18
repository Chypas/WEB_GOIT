import json
from json import loads

import scrapy
from itemadapter import ItemAdapter
from scrapy.item import Item, Field
from scrapy.crawler import CrawlerProcess
from mongoengine import disconnect
from models import Authors, Quotes


def seed_authors(file):
    json_file = file.read()
    data = loads(json_file)
    for authors in data:
        author = Authors(
            fullname=authors["fullname"],
            date_born=authors["date_born"],
            born_location=authors["born_location"],
            bio=authors["bio"],
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


class QuoteItem(Item):
    tags = Field()
    author = Field()
    quote = Field()


class AuthorItem(Item):
    fullname = Field()
    date_born = Field()
    born_location = Field()
    bio = Field()


class MainPipline:
    quotes = []
    authors = []

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if "fullname" in adapter.keys():
            self.authors.append(adapter.asdict())
        if "quote" in adapter.keys():
            self.quotes.append(adapter.asdict())
        return item

    def close_spider(self, spider):
        with open("quotes.json", "w", encoding="utf-8") as fd:
            json.dump(self.quotes, fd, ensure_ascii=False)
        with open("authors.json", "w", encoding="utf-8") as fd:
            json.dump(self.authors, fd, ensure_ascii=False)


def parse_author(response, *args):
    content = response.xpath("/html//div[@class='author-details']")
    fullname = content.xpath("h3[@class='author-title']/text()").get().strip()
    date_born = (
        content.xpath("p/span[@class='author-born-date']/text()").get().strip()
    )
    born_location = (
        content.xpath("p/span[@class='author-born-location']/text()").get().strip()
    )
    bio = content.xpath("div[@class='author-description']/text()").get().strip()
    yield AuthorItem(
        fullname=fullname, date_born=date_born, born_location=born_location, bio=bio
    )


class MainSpider(scrapy.Spider):
    name = "main_spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com"]
    custom_settings = {"ITEM_PIPELINES": {MainPipline: 100}}
    START_INDEX = 0

    def parse(self, response, *args):
        for el in response.xpath("/html//div[@class='quote']"):
            tags = [
                e.strip()
                for e in el.xpath("div[@class='tags']/a[@class='tag']/text()").extract()
            ]
            author = el.xpath("span/small[@class='author']/text()").get().strip()
            quote = el.xpath("span[@class='text']/text()").get().strip()
            yield QuoteItem(tags=tags, author=author, quote=quote)
            yield response.follow(
                url=self.start_urls[self.START_INDEX]
                + el.xpath("span/a/@href").get().strip(),
                callback=parse_author,
            )
            next_link = response.xpath("//li[@class='next']/a/@href").get()
            if next_link:
                yield scrapy.Request(
                    url=self.start_urls[self.START_INDEX] + next_link.strip()
                )


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(MainSpider)
    process.start()
    with open("authors.json", "r", encoding="utf-8") as file:
        seed_authors(file)
    with open("quotes.json", "r", encoding="utf-8") as file:
        seed_quotes(file)
    disconnect()
    print("End")
