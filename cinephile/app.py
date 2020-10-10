from scrapy.crawler import CrawlerProcess
from cinephile.spiders.factory import SpidersFactory
from cinephile.spiders.pornhub.main import PornhubVideosMainSpider
from cinephile.config import Config
from scrapy.utils.log import configure_logging
from twisted.internet import reactor
from twisted.internet.task import deferLater
import logging
import sys
import signal


def signal_handler(signal, frame):
    print("\npcinephile exiting gracefully")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
# This call is needed to hack the Scrapy logging issues
configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
interval = Config.internal()

process = CrawlerProcess(settings={
    'ITEM_PIPELINES': {
        'cinephile.pipelines.redis.RedisPipeline': 300,
    },
    'DOWNLOAD_DELAY': Config.download_delay(),
    'DEPTH_LIMIT': Config.depth_limit(),
    'COOKIES_ENABLED': False,
    'LOG_LEVEL': Config.log_level(),
})


def sleep(self, *args, seconds):
    """Non blocking sleep callback"""
    return deferLater(reactor, seconds, lambda: None)


def _crawl(result, spider):
    deferred = process.crawl(spider)
    # deferred.addCallback(lambda results: print('sleep...'))
    deferred.addCallback(sleep, seconds=Config.internal())
    deferred.addCallback(_crawl, spider)
    return deferred


if __name__ == "__main__":
    spiders_factory = SpidersFactory()
    spider = spiders_factory.create_spider(Config.spider())
    _crawl(None, spider)
    logging.getLogger().setLevel(Config.log_level())
    process.start()
