def is_prime(n):

    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """

    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:

            return False
            
    return True
