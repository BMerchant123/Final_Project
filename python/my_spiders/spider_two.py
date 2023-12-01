import scrapy
import csv
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os

class spider_one(scrapy.Spider):
## First Read through our dataset and select the url's
    name = 'spider_two'
    def start_requests(self):
        csv_file_path = os.path.abspath('datasets/malware_dataset.csv')
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                url = row[0]
                yield scrapy.Request(url=url, callback=self.parse)

## Scrape the URL IP address
    def parse(self, response):
        ip_address = response.json().get('origin')
        self.log(ip_address)

    def run_spider_two(self):
        process = CrawlerProcess(get_project_settings())
        process.crawl(self)
        process.start()
        process.stop()