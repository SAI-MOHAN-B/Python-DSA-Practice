class Solution:
    def swap(self,arr,first,second):
        temp = arr[first]
        arr[first] = arr[second]
        arr[second] = temp
    def findDuplicate(self, arr: List[int]) -> int:
        i = 0
        while i < len(arr):
            correct_index = arr[i] - 1
            if arr[i] < len(arr) and arr[i] != arr[correct_index]:
                self.swap(arr,i,correct_index)
            else:
                i+=1
        for i in range(len(arr)):
            # here we are checking the whether 
            # the element is equal to index+1 
            # then 2 cases are there
            # 1. if the element is not 
            # equal then swap
            # 2. suppose if it is duplicated
            # then return that element
            if arr[i]!= i+1:
                return arr[i]

