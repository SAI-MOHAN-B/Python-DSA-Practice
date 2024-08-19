import math
def recur_binary(arr,target,start,end):
    if start > end:
        return -1
    mid = math.floor(start+(end-start)/2)
    if target == arr[mid]:
        return mid
    if target < arr[mid]:
        return recur_binary(arr,target,start,end-1)
    else:
        return recur_binary(arr,target,mid+1,end)
res = recur_binary([12,13,14,15],15,0,3)
print(res)
