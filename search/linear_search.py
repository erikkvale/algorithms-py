def linear_search(_list, item):
    """
    Conducts a linear search through sorted/unsorted list of integers

    >>> a_list = [2, 5, 6, 10, 3, 1]
    >>> item = 10
    >>> linear_search(a_list, item)
    3

    >>> a_list = [2, 5, 6, 10, 3, 1]
    >>> item = -1
    >>> linear_search(a_list, item) is None
    True

    """
    for idx, n in enumerate(_list):
        if n == item:
            return idx
    return None