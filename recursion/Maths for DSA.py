import math
def test_Data(n):
   # here b represents the base of the number whether it is base 2 or base 10
   b = 2
   ans = int(math.log(n)/math.log(b))+1
   return ans
res = test_Data(10)
print(res)
    
