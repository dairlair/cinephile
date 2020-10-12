from injector import singleton, Binder
from cinephile.core import CacheInterface, PublisherInferface
from cinephile.config import Config
from cinephile.cache.redis import RedisCache
from cinephile.publisher.amqp import AMQPPublisher


def configure(binder: Binder) -> None:
    binder.bind(CacheInterface, create_cache, scope=singleton)
    binder.bind(PublisherInferface, create_publisher, scope=singleton)


def create_cache() -> CacheInterface:
    return RedisCache(Config.cache_url())


def create_publisher() -> PublisherInferface:
    exchange = Config.amqp_exchange()
    routing_key = Config.amqp_routing_key()
    return AMQPPublisher(Config.amqp_url(), exchange, routing_key)
