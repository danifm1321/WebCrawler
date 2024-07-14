import scrapy
from scraper.items import NewsEntryScraper

class HackerNewsSpider(scrapy.Spider):
    name = "hacker_news"  # Spider name used when running Scrapy

    start_urls = ['https://news.ycombinator.com/']  # Starting URL for the spider

    def parse(self, response):
        """
        Parses the response from the Hacker News website and extracts news entries.

        Args:
            response (scrapy.http.Response): The response object containing the HTML content of the page.

        Yields:
            dict: A dictionary representing a news entry with attributes like 'number', 'title', 'points', 'number_of_comments'.
        """
        i = 0  # Counter to limit the number of news entries processed

        # Iterate over each news item on the page
        for item in response.xpath('//tr[@class="athing"]'):

            if i >= 30:  # Limit to processing only the first 30 news items
                break

            news = NewsEntryScraper()  # Create a new instance of NewsEntryScraper (assuming it's defined elsewhere)

            # Extract the news number (removing the final dot)
            news['number'] = item.xpath('.//span[@class="rank"]/text()').get()[:-1]

            # Extract the news title
            news['title'] = item.xpath('.//span[@class="titleline"]/a/text()').get()

            # Extract the points (removing " points" if present)
            points = item.xpath('following-sibling::tr[1]//span[@class="score"]/text()').get()
            if points:
                news['points'] = points.split()[0]
            else:
                news['points'] = '0'  # Default to '0' if no points found

            # Extract the number of comments (removing " comments" if present)
            comments_text = item.xpath('following-sibling::tr[1]//a[contains(text(), "comments")]/text()').get()
            if comments_text:
                news['number_of_comments'] = comments_text.split()[0]
            else:
                news['number_of_comments'] = '0'  # Default to '0' if no comments found

            yield news  # Yield the news entry dictionary

            i += 1  # Increment the counter for the next iteration