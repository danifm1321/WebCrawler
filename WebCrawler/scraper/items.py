# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsEntryScraper(scrapy.Item):
    """
    Defines the structure of a news entry item to be scraped.
    """

    # Define fields for the news entry
    number = scrapy.Field()             # Holds the number of the news entry
    title = scrapy.Field()              # Holds the title of the news entry
    points = scrapy.Field()             # Holds the points of the news entry
    number_of_comments = scrapy.Field() # Holds the number of comments on the news entry

    pass