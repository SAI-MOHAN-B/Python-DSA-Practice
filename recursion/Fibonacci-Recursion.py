def fibo(n):
    if n < 2:
        return n
    # below is the recurrence relation
    return fibo(n-1) + fibo(n-2)
fibo(4)