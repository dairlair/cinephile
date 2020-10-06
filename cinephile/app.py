import scrapy
from scrapy.crawler import CrawlerProcess
from cinephile.spiders.nasa.launches import NasaLaunchesSpider

print ('Application is running....')

process = CrawlerProcess(settings={
    "FEEDS": {
        "items.json": {"format": "json"},
    },
})

process.crawl(NasaLaunchesSpider)
process.start()