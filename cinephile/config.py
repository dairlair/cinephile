import os
from cinephile.spiders.pornhub.main import PornhubVideosMainSpider


class Config(object):
    @staticmethod
    def log_level() -> str:
        return os.environ.get('LOG_LEVEL', 'WARNING')

    @staticmethod
    def internal() -> float:
        return float(os.environ.get('INTERVAL', 60))

    @staticmethod
    def cache_url() -> str:
        return os.environ.get('CACHE_URL', 'redis://localhost:6379/0')

    @staticmethod
    def download_delay() -> int:
        return int(os.environ.get('DOWNLOAD_DELAY', 2))

    @staticmethod
    def depth_limit() -> int:
        return int(os.environ.get('DEPTH_LIMIT', 2))

    @staticmethod
    def spider() -> str:
        return os.environ.get('SPIDER', PornhubVideosMainSpider.name)
