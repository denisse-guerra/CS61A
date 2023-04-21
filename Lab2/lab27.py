def fibonacciN(n):

	"""Return the nth Fibonacci number.
    Fibonacci Numbers is a series of numbers in which each number is the sum of the two preceding numbers

    >>> fibonacciN(5) # 1, 1, 2, 3, 5
    5
    >>> fibonacciN(7) 
    13
    """

	prev, curr = 0,1
	k = 0

	while k < n:
		prev, curr = curr, prev + curr
		k = k + 1
		
	return prev