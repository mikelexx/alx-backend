#!/usr/bin/env python3
"""
Copy index_range from previous task and the given class from task
docs into your code
copy the index_range from previous task as well
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size) -> Tuple[int, int]:
    """"
    Args:
        page_size(int): size of each query result
        page(int): page number(e.g a query count/ith page)
    Returns:
            a tuple containing:
                start_index: (int) starting index for that page.
                end_index: end index of that page.
    """
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Args:
            page (int): ith page to extract
            page_size: length of each page
        Returns: appropriate page of dataset(i.e correct list of rows)
        """
        assert (type(page), type(page_size)) == (int, int)
        assert page > 0 and page_size > 0
        (start_index, end_index) = index_range(page, page_size)
        server = Server()
        data: List[List] = server.dataset()
        res: List[List] = []
        if end_index > len(data):
            return res
        res.append(data[start_index:end_index])
        return res
