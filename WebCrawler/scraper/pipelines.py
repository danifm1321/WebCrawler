# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import os

class JsonWriterPipeline:
    """
    Pipeline for writing scraped items to a JSON file.
    """

    def open_spider(self, spider):
        """
        Called when the spider is opened.

        Args:
            spider (scrapy.Spider): The Spider object that is opened.
        """
        # Create 'results' directory if it doesn't exist
        os.makedirs('results', exist_ok=True)
        # Open 'output.json' file for writing
        self.file = open('results/output.json', 'w')

    def close_spider(self, spider):
        """
        Called when the spider is closed.

        Args:
            spider (scrapy.Spider): The Spider object that is closed.
        """
        # Close the JSON file
        self.file.close()

    def process_item(self, item, spider):
        """
        Process each item scraped by the spider.

        Args:
            item (scrapy.Item): The scraped item.
            spider (scrapy.Spider): The Spider object that is processing the item.

        Returns:
            scrapy.Item: The processed item.
        """
        # Convert item to dictionary and serialize to JSON
        line = json.dumps(dict(item)) + "\n"
        # Write JSON line to the file
        self.file.write(line)
        # Return the processed item
        return item