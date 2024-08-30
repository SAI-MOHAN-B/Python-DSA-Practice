class Solution:
    def helper(self,num1: int,num2: int,c=0):
        if num1 == 0 or num2  == 0:
            return c
        if num1 >= num2:
            res = num1 - num2
            return self.helper(res,num2,c+1)
        res1 = num2 - num1
        return self.helper(num1,res1,c+1)

    def countOperations(self, num1: int, num2: int) -> int:
        return self.helper(num1,num2)
        
