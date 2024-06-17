import math
def floor_number(arr,target):
    start = 0
    end = len(arr) - 1
    while(start<=end):
        mid = math.floor(start+(end-start)/2)
        if target == arr[mid]:
            return mid
        if target > arr[mid]:
            start = mid+1
        if target < arr[mid]:
            end = mid - 1
    return arr[end]    
res = floor_number([2,3,5,9,14,16,18],15)
print(res)
