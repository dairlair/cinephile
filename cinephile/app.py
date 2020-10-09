from scrapy.crawler import CrawlerProcess
from cinephile.spiders.pornhub.main import PornhubVideosMainSpider
import logging


print('Application is running....')

process = CrawlerProcess(settings={
    'ITEM_PIPELINES': {
        'cinephile.pipelines.redis.RedisPipeline': 300,
    },
    'LOG_LEVEL': logging.WARNING,
    'DOWNLOAD_DELAY': 2,
    'DEPTH_LIMIT': 1
})

process.crawl(PornhubVideosMainSpider)
process.start()
