def fact(n):
    if n == 0 or n == 1:
        return 1
    # the recurrence relation decides here 
    # 3 means 3*2*1
    # the underlying condition is that
    # n*n-1*n-2
    return n*fact(n-1)
fact(3)
