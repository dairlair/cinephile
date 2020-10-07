import scrapy
from scrapy.crawler import CrawlerProcess
from cinephile.spiders.nasa.launches import NasaLaunchesSpider
from cinephile.spiders.pornhub.main import PornhubMainSpider
import logging

print ('Application is running....')

process = CrawlerProcess(settings={
    'ITEM_PIPELINES': {
        'cinephile.pipelines.redis.RedisPipeline': 300,
    },
    'LOG_LEVEL': logging.WARNING,
    'DOWNLOAD_DELAY': 2,
    'DEPTH_LIMIT': 10
})

process.crawl(PornhubMainSpider)
process.start()