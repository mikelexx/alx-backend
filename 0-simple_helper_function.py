#!/usr/bin/env python3
"""
Write a function named index_range that takes two integer arguments
page and page_size.

The function should return a tuple of size two containing
a start index and an end index corresponding to the
range of indexes to return in a list for those
particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""
from typing import Tuple


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
