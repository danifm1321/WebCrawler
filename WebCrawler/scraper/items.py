# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsEntry(scrapy.Item):
    number = scrapy.Field()
    title = scrapy.Field()
    points = scrapy.Field()
    number_of_comments = scrapy.Field()
    pass
