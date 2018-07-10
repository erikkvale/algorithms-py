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


def greet(name):
    print("Hello, {}!".format(name))
    greet_two(name)
    print("Getting ready to say goodbye...")
    bye()

def greet_two(name):
    print("How are you, {}?".format(name))

def bye():
    print("Ok, bye")

if __name__=='__main__':
    greet("maggie")
    # import doctest
    # doctest.testmod()
