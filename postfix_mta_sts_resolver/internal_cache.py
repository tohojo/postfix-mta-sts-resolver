import collections
import time

class InternalLRUCache(object):
    def __init__(self, capacity=10000):
        self._capacity = capacity
        self._cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self._cache.pop(key)
            self._cache[key] = value
            return value
        except KeyError:
            return None

    def set(self, key, value):
        try:
            self._cache.pop(key)
        except KeyError:
            if len(self._cache) >= self._capacity:
                self._cache.popitem(last=False)
        self._cache[key] = value
