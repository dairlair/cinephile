from cinephile.core import CacheInterface
from redis import Redis, RedisError
import logging
import sys

class RedisCache(CacheInterface):
    def __init__(self, url: str):
        try:
            self.conn = Redis.from_url(url)
            logging.info(f'Successfully connected to Redis at [{url}]')
        except RedisError:
            logging.error(f"Couldn't connect to the Redis broker. Please, check the Redis is available with the specified URL: [{url}]")
            sys.exit(2)

    def set_if_not_exists(self, key: str) -> bool:
        return True