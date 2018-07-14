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


def factorial(n):
    """
    Factorial, written n! n * (n - 1) * (n - 2) * ... (1)
    """
    # Base case
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__=='__main__':
    print(factorial(3))
