def and_add(f, n):

    """Return a new function. This new function takes an
    argument x and returns f(x) + n.

    >>> def square(x):
    ...     return x * x
    >>> new_square = and_add(square, 3)
    >>> new_square(4) # 4 * 4 + 3
    19
    """

    def new_function(x):

        return f(x) + n
        
    return new_function
