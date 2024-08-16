#!/usr/bin/env python3
"""
Hypermedia pagination
"""
import csv
import math
from typing import Any, Dict, List, Tuple, Union


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
        if end_index > len(data):
            return []
        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        provides Hypermedia for get_page api endpoint
        Args:
            page: current page number
            page_size: size of each page from available data
        Returns: a dictionary containing the follwoing key-value pairs
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None
                        if no previous page
            total_pages: the total number of pages in the dataset as
                    an integer
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)
        data = self.get_page(page, page_size)
        data_page_size = len(data)
        next_page = page + data_page_size
        if next_page > total_pages:
            next_page = None
        prev_page = page - 1 if page > 1 else None
        return {
            'page_size': data_page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
