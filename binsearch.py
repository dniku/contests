def sqrt_both_inclusive(n):
    lower = 0
    upper = n
    while (lower + 1 < upper):
        middle = lower + (upper - lower) // 2
        if (middle * middle <= n):
           lower = middle
        else:
           upper = middle
    return (lower, upper)
