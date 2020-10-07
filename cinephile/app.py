import scrapy
from scrapy.crawler import CrawlerProcess
from cinephile.spiders.nasa.launches import NasaLaunchesSpider
import logging

print ('Application is running....')

process = CrawlerProcess(settings={
    'ITEM_PIPELINES': {
        'cinephile.pipelines.redis.RedisPipeline': 300,
    },
    'LOG_LEVEL': logging.WARNING,
})

process.crawl(NasaLaunchesSpider)
process.start()