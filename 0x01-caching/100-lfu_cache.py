#!/usr/bin/env python3
"""
implementing LFU cache replaecment policy caching system
"""
from collections import Counter

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    caching system that uses LFU cache replaecment policy
    """

    def __init__(self) -> None:
        super().__init__()
        self.lfu_counter = Counter()

    def put(self, key, item):
        """
       assigns to the dictionary self.cache_data the
        item value for the key key.
        If the number of items in self.cache_data is
        higher that BaseCaching.MAX_ITEMS:
            you must discard the least frequently used item in cache
            (LFU algorithm)
            you must print DISCARD: with the key discarded
            and following by a new line
        """
        if key and item:
            # print(f'putting {key}')
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                lfu_key, min_freq = None, float('inf')
                for keyC, val in self.lfu_counter.items():
                    if val < min_freq:
                        min_freq = val
                        lfu_key = keyC
                del self.cache_data[lfu_key]
                del self.lfu_counter[lfu_key]
                print(f'DISCARD: {lfu_key}')
            self.lfu_counter[key] += 1
        # print(f'after putting {key}')
        # print(f'curr-cache---> {self.cache_data.items()}')
        # print(f'curr-cache-counter---> {self.lfu_counter.items()}')

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in
        self.cache_data, return None.
        """
        # print(f'get {key}')
        res = self.cache_data.get(key)
        if res:
            self.lfu_counter[key] += 1
        return res
