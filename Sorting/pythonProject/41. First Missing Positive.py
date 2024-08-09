class Solution:
    def swap(self,arr,first,second):
        temp = arr[first]
        arr[first] = arr[second]
        arr[second] = temp
    def firstMissingPositive(self, arr: List[int]) -> int:
        i = 0
        while i < len(arr):
            correct_index = arr[i] - 1
            if arr[i] > 0 and arr[i] < len(arr) and arr[i]!=arr[correct_index]:
                self.swap(arr,i,correct_index)
            else:
                i+=1
        for i in range(len(arr)):
            if arr[i] != i+1:
                return i+1
        return len(arr)+1
        
