import os


class Config(object):
    @staticmethod
    def log_level() -> str:
        return os.environ.get('LOG_LEVEL') or 'WARNING'

    @staticmethod
    def internal() -> float:
        return float(os.environ.get('INTERVAL', 10))

    @staticmethod
    def cache_url() -> str:
        return os.environ.get('CACHE_URL') or 'redis://localhost:6379/0'
