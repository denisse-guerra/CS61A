def hailstone(n, count = 0):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """

    print(n)
    if n == 1:
        return count
    elif n % 2 == 0:
        return hailstone(n // 2, count + 1)
    else:
        return hailstone(3 * n + 1, count + 1)
