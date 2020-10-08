import os

class Config(object):
    @staticmethod
    def cache_url() -> str:
        return os.environ.get('CACHE_URL') or 'redis://localhost:6379/0'