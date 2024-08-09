class Solution:
    def swap(self,arr,first,second):
        temp = arr[first]
        arr[first] = arr[second]
        arr[second] = temp
    def findErrorNums(self, arr: List[int]) -> List[int]:
        i = 0
        temp = []
        while i < len(arr):
            correct = arr[i] - 1
            if arr[i] != arr[correct]:
                self.swap(arr,i,correct)
            else:
                i+=1
        for i in range(len(arr)):
            if arr[i] != i+1:
                # this is for the element which is in wrong index(duplicated)
                temp.append(arr[i])
                # this is for number that is missing(usually index+1 will be missing)
                temp.append(i+1)
               
        return temp
        
