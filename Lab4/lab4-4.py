def is_prime(n, i=2):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    if n == i:
        return True

    elif n % i == 0:
        return False
        
    else:
        return is_prime(n, i+1)
