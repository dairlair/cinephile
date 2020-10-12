from cinephile.core import CacheInterface
from redis import Redis, RedisError, from_url
import logging
import sys


class RedisCache(CacheInterface):
    redis: Redis

    def __init__(self, url: str):
        try:
            self.redis = from_url(url)
            logging.info(f'Successfully connected to Redis at [{url}]')
        except RedisError:
            logging.error(f"Couldn't connect to the Redis broker at [{url}]")
            sys.exit(2)

    def set_if_not_exists(self, key: str, value: str) -> bool:
        return self.redis.setnx(key, value)
