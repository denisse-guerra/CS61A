def group_by(seq, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """
    d = {}
    for item in seq:

        key = fn(item)
        if key not in d:
            d[key] = []
        d[key].append(item)
        
    return d