def find_smallest(_list):
    """
    Finds the smallest integer in an array

    >>> demo_list = [4, 5 , 2, 6]
    >>> find_smallest(demo_list)
    2
    """
    smallest = _list[0]
    smallest_idx = 0
    for idx, num in enumerate(_list):
        if num < smallest:
            smallest = num
            smallest_idx = idx
    return smallest_idx


def selection_sort(_list):
    """
    Uses helper function to sort list
    >>> demo_list = [4, 5, 2, 6]
    >>> selection_sort(demo_list)
    [2, 4, 5, 6]
    """
    new_list = []
    for i in range(len(_list)):
        smallest = find_smallest(_list)
        new_list.append(_list.pop(smallest))
    return new_list

if __name__=='__main__':
    import doctest
    doctest.testmod()
