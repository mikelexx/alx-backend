#!/usr/bin/env python3
"""
implementing LIFO cache replaecment policy caching system
"""
from collections import deque

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    caching system that uses LIFO cache replaecment policy
    """

    def __init__(self) -> None:
        super().__init__()
        self.queue = deque([])

    def put(self, key, item):
        """
       assigns to the dictionary self.cache_data the
        item value for the key key.
        If the number of items in self.cache_data is
        higher that BaseCaching.MAX_ITEMS:
            you must discard the last item put in cache
            (LIFO algorithm)
            you must print DISCARD: with the key discarded
            and following by a new line
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                last_key = self.queue.pop()
                del self.cache_data[last_key]
                print(f'DISCARD: {last_key}')
            self.queue.append(key)

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in
        self.cache_data, return None.
        """
        return self.cache_data.get(key)
