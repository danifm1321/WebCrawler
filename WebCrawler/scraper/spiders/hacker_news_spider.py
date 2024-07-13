import scrapy
from scraper.items import NewsEntry

class HackerNewsSpider(scrapy.Spider):
    name = "hacker_news"

    start_urls = ['https://news.ycombinator.com/']

    def parse(self, response):

        i = 0

        for item in response.xpath('//tr[@class="athing"]'):

            if i >= 30:
                break

            news = NewsEntry()

            #In order to get only the number, we remove the final dot
            news['number'] = item.xpath('.//span[@class="rank"]/text()').get()[:-1]
            news['title'] = item.xpath('.//span[@class="titleline"]/a/text()').get()

            #In order to get only the points, we remove the " points"
            points = item.xpath('following-sibling::tr[1]//span[@class="score"]/text()').get()
            if points:
                news['points'] = points.split()[0]
            else:
                news['points'] = 0
            
            # Extract the number of comments
            comments_text = item.xpath('following-sibling::tr[1]//a[contains(text(), "comments")]/text()').get()
            if comments_text:
                #In order to get only the number of comments, we remove the " comments"
                news['number_of_comments'] = comments_text.split()[0]
            else:
                news['number_of_comments'] = '0'  # Default to '0' if none found

            yield news

            i += 1