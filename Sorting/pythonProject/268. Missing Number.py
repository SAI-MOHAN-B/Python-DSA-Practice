class Solution:
    def swap(self,arr,first,second):
        temp = arr[first]
        arr[first] = arr[second]
        arr[second] = temp

    def missingNumber(self, arr: List[int]) -> int:
        i = 0
        while i < len(arr):
            # since we are starting from 0, then we removed
            # the traditional value formula
            # index = value - 1
            correct = arr[i]
            # below condition checks the array out of bound case
            if arr[i] < len(arr) and arr[i] != arr[correct]:
                self.swap(arr,i,correct)
            else:
                i+=1
        for i in range(len(arr)):
            if arr[i] != i:
                return i
        # this is for the case where the number does'nt exists in the array
        return len(arr)
