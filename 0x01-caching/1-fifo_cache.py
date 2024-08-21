#!/usr/bin/env python3
"""
implementing FIFO cache replaecment policy caching system
"""
from collections import deque

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    caching system that uses FIFO cache replaecment policy
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
            you must discard the first item put in cache
            (FIFO algorithm)
            you must print DISCARD: with the key discarded
            and following by a new line
        """
        if key and item:
            self.queue.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                first_key = self.queue.popleft()
                del self.cache_data[first_key]
                print(f'DISCARD: {first_key}')

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in
        self.cache_data, return None.
        """
        return self.cache_data.get(key)
