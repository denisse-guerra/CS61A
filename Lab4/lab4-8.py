def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.
    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def count_d(d, number):
        if number < 10 and number == d:
            return 1
        elif number < 10 and number != d:
            return 0
        elif number % 10 == d:
            return 1 + count_d(d, number // 10)
        else:
            return count_d(d, number // 10)

    def helper(n):
        if n < 10:
            return 0
        else:
            return count_d(10 - n % 10, n // 10) + helper(n // 10)

    return helper(n)