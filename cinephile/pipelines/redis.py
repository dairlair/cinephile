from injector import Injector
from cinephile.core import CacheInterface, PublisherInferface
from cinephile.dependencies import configure
import logging

# @TODO Divede this complex pipeline into the three
# different pipelines: UniqalityPipeline, EnrichmentPipeline PublishingPipeline
# EnrichmentPipeline should add some common attributes to parsed 
# items, like a foundAt, spider, type.
class RedisPipeline(object):
    cache: CacheInterface
    publisher: PublisherInferface

    def __init__(self, cache: CacheInterface, publisher: PublisherInferface):
        self.cache = cache
        self.publisher = publisher

    @classmethod
    def from_crawler(self, crawler):
        injector = Injector([configure])
        cache: CacheInterface = injector.get(CacheInterface)
        publisher: PublisherInferface = injector.get(PublisherInferface)
        return RedisPipeline(cache, publisher)

    def process_item(self, item: dict, spider):
        url = item['url']
        # Wrong item received, skip
        if url is None:
            logging.warning("Video with wrong URL received, spider: " + spider.name)
            return None

        result = self.cache.set_if_not_exists('url:' + url, 1)
        if result is False:
            return None

        self.publisher.publish(item)
        return item
