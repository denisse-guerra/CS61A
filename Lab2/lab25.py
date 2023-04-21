def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) 
    >>> x
    6
    """
    sum = 0
    while n > 0:
        # n, sum = n // 10, sum + n % 10
        n, d = n // 10, n % 10
        sum += d
    return sum