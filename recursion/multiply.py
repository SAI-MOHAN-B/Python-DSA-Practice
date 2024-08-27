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
