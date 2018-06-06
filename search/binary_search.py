def binary_search(_list, item):
    """
    Conducts a binary search on a sorted list of integers

    >>> even_list = [2, 5, 6, 10, 3, 1]
    >>> item = 5
    >>> binary_search(even_list, item)
    3

    >>> odd_list = [2, 5, 6, 10, 3, 1, 9]
    >>> item = 9
    >>> binary_search(odd_list, item)
    5

    >>> _list = [2, 1, 3]
    >>> item = -1
    >>> binary_search(_list, item) is None
    True

    """
    sorted_list = sorted(_list)
    low = 0
    high = len(sorted_list)

    while low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
    return None



if __name__=='__main__':
    import doctest
    doctest.testmod()

