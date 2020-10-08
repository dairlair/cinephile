from injector import Injector
from cinephile.core import CacheInterface

class RedisPipeline(object):
    cache: CacheInterface
    def __init__(self):
        injector = Injector()
        self.cache = injector.get(CacheInterface)

    def process_item(self, item: dict, spider):
        url = item['url']
        result = self.cache.set_if_not_exists('url:' + url)
        
        if result == False:
            print(f'URL {url} is already processed and will be skipped')
            return None

        print('Items is processed:')
        print(item)
        return item 

    def open_spider(self, spider):
        print('Open the Redis connection')

    def close_spider(self, spider):
        print('Close the Redis connection')