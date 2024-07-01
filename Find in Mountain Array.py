# https://leetcode.com/problems/find-in-mountain-array/description/
import math
def order_agnostic_bs(arr,target,start,end):
    # find whether the array is sorted in ascending or descending
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
def peak_index(arr):
    start = 0
    end = len(arr) - 1 
    while start<end:
        mid = math.floor(start+(end-start)/2)
        if arr[mid]>arr[mid+1]:
            end = mid
        else:
            start = mid + 1 
        return start
def search(arr,target):
    peak = peak_index(arr)
    first_try = order_agnostic_bs(arr,target,0,peak)
    if first_try != -1:
        return first_try
    # try to search in second half
    return order_agnostic_bs(arr,target,peak+1,len(arr) - 1)
res = search([0,1,2,4,2,1],5)
print(res)
    
