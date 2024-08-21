#!/usr/bin/env python3
"""
implementing LRU cache replaecment policy caching system
"""
from collections import Counter

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    caching system that uses LRU cache replaecment policy
    """

    def __init__(self) -> None:
        super().__init__()
        self.lru_counter = Counter()

    def put(self, key, item):
        """
       assigns to the dictionary self.cache_data the
        item value for the key key.
        If the number of items in self.cache_data is
        higher that BaseCaching.MAX_ITEMS:
            you must discard the least recently used item in cache
            (LRU algorithm)
            you must print DISCARD: with the key discarded
            and following by a new line
        """
        if key and item:
            # print(f'putting {key}')
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                lru_key, min_rank = None, float('inf')
                for keyC, val in self.lru_counter.items():
                    if val < min_rank:
                        min_rank = val
                        lru_key = keyC
                del self.cache_data[lru_key]
                del self.lru_counter[lru_key]
                print(f'DISCARD: {lru_key}')
            if len(self.lru_counter) > 0:
                max_rank = max(self.lru_counter.values())
                self.lru_counter[key] = max_rank + 1
            else:
                self.lru_counter[key] = 0
        # print(f'after putting {key}')
        # print(f'curr-cache---> {self.cache_data.items()}')
        # print(f'curr-cache-counter---> {self.lru_counter.items()}')

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in
        self.cache_data, return None.
        """
        # print(f'get {key}')
        res = self.cache_data.get(key)
        if res:
            recent_count = max(self.lru_counter.values())
            self.lru_counter[key] = recent_count + 1
        return res
