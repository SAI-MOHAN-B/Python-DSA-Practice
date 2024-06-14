import math
def orderagn(arr,target):
    start = 0
    end = len(arr)-1
    isAsc = arr[start] < arr[end]
    while(start<=end):
        mid = math.floor(start+(end-start)/2)
        if isAsc:
            if target<arr[mid]:
                end = mid-1
            elif target>arr[mid]:
                start = mid+1 
            else:
                return mid
        else:
            if target<arr[mid]:
                start = mid+1
            elif target>arr[mid]:
                end = mid-1
            else:
                return mid
    return -1
res = orderagn([10,9,8,7,6,5,4,3,2,1],4)
print(res)
