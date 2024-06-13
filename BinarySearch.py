import math
def binary_search(arr,target):
    start = 0
    end = len(arr)-1
    while(start<=end):
        mid = math.floor(start+(end-start)/2)
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            start = mid+1
        else:
            end = mid-1
    return -1
res = binary_search([12,13,14,15,16,17,18,19,20],200)
print(res)
