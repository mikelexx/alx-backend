#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i]
                for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Deletion-resilient function for  hypermedia pagination
        Args:
            index (int): starting index of the page to be returned
            page_size (int): length of data chuck to extract from dataset
        Returns:
            data list where The goal here is that if between two
            queries, certain rows are removed from the dataset, the
            user does not miss items from dataset when changing page.
        """
        indexed_dataset: Dict[int, List] = self.indexed_dataset()
        indexed_dataset_len: int = len(indexed_dataset)
        assert type(index) is int
        assert index >= 0 and index <= indexed_dataset_len
        start_index: Union[int, None] = None
        data: List[List] = []
        counter_index: int = index
        while counter_index < indexed_dataset_len and len(data) < page_size:
            data_entry = indexed_dataset.get(counter_index)
            if data_entry:
                data.append(data_entry)
                if not start_index:
                    start_index = counter_index
            counter_index += 1

        data_len: int = len(data)
        next_index: Union[
            int, None] = start_index + data_len if start_index else None
        return {
            'index': index,
            'data': data,
            'page_size': data_len,
            'next_index': next_index
        }
