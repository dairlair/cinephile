from injector import singleton, Binder
import sys
import logging
from cinephile.core import CacheInterface
from cinephile.config import Config
from cinephile.cache.redis import RedisCache


def configure(binder: Binder) -> None:
    binder.bind(CacheInterface, to=create_redis_client, scope=singleton)
    

def create_redis_client() -> CacheInterface:
    return RedisCache(Config.cache_url)

