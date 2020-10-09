from injector import Injector
from cinephile.core import CacheInterface
from cinephile.dependencies import configure
import logging


class RedisPipeline(object):
    cache: CacheInterface

    def __init__(self, cache: CacheInterface):
        self.cache = cache

    @classmethod
    def from_crawler(self, crawler):
        injector = Injector([configure])
        cache: CacheInterface = injector.get(CacheInterface)
        return RedisPipeline(cache)

    def process_item(self, item: dict, spider):
        url = item['url']
        result = self.cache.set_if_not_exists('url:' + url, 1)

        if result is False:
            logging.info(f'URL {url} is already processed and will be skipped')
            return None

        logging.info('Items is processed:')
        logging.error(item)
        return item

    def open_spider(self, spider):
        # print('Open the Redis connection')
        pass

    def close_spider(self, spider):
        # print('Close the Redis connection')
        pass
