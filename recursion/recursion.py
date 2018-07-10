def countdown(i):
    """
    >>> countdown(3)
    3
    2
    1
    >>> countdown(0)
    0
    """
    # Base case
    if i <= 0:
        return 0
    # Recursive case
    else:
        print(i)
        countdown(i - 1)


if __name__=='__main__':
    import doctest
    doctest.testmod()
