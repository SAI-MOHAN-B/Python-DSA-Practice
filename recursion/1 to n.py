# recursion for 1 to n
def funrev(n):
    if n == 0:
        return
    print(n)
    funrev(n-1)
    print(n)
funrev(5)
