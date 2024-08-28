# multiplication of individual digits
import math
def digit_sum(n):
    if n%10 == n:
        return n
    return (n%10)*(digit_sum(n//10))
res = digit_sum(1342)
print(res)

# sum of digits in recursion
import math
def digit_sum(n):
    if n== 0:
        return 0
    return (n%10)+(digit_sum(n//10))
res = digit_sum(13)
print(res)

# printing the numbers in reverse order
import math
def digi(n):
    if n == 0:
        return
    print(n)
    digi(n=n-1)
digi(5)

# reverse a number
import math
def digi(n):
    if n<10:
        print(n)
        return n
    print(n%10)
    digi(n//10)
digi(12345)


# Counting the number of zero's in the given number
import math


def count_num(n, c):
    return helper(n, c)


def helper(n, c):
    if n == 0:
        return c
    rem = n % 10
    if rem == 0:
        return helper(n // 10, c + 1)
    return helper(n // 10, c)


res = count_num(30204, 0)
print(res)
