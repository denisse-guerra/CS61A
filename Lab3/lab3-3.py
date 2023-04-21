def make_keeper(n): 
    """Returns a function which takes one parameter cond and prints
    out all integers 1..i..n  where calling cond(i) returns True.
 
    >>> def is_even(x):
    ... #Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def inner(cond):

        for i in range(1, n + 1):
            if cond(i):
                print(i)
                
    return inner
