from abc import ABC, abstractmethod

class CacheInterface(ABC):
    """
        CacheInterface is used to declare dependency from the cache.

        The cache must provide functionality to:
            * set key to value if it isn't set before (the operation like a Redis SETNX)
    """

    @abstractmethod
    def set_if_not_exists(self, key: str) -> bool:
        """
        Must return True if key does not exist and has been set successfully, False otherwise.

        :param key: 
        """
        raise NotImplementedError
