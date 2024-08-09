class Solution:
    def swap(self,arr,first,second):
        temp = arr[first]
        arr[first] = arr[second]
        arr[second] = temp
    def findDuplicates(self, arr: List[int]) -> List[int]:
        i = 0
        temp = []
        if len(arr) == 1:
            return []
        while i < len(arr):
            correct_index = arr[i] - 1
            if arr[i]!= arr[correct_index]:
                self.swap(arr,i,correct_index)
            else:
                i+=1
        for i in range(len(arr)):
            if arr[i] != i+1:
                temp.append(arr[i])
        return temp


        
