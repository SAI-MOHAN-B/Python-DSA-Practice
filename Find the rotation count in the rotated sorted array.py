import math
def binary_search(arr,target,start,end):
    while start<=end:
        mid = math.floor(start+(end-start)/2)
        if target == arr[mid]:
            return mid
        if target < arr[mid]:
            end = mid - 1 
        if target > arr[mid]:
            start = mid + 1 
    return -1
def pivot_fun(arr):
    start = 0
    end = len(arr) -1
    while start<=end:
        mid = math.floor(start+(end-start)/2)
        if mid < end and arr[mid] > arr[mid+1]:
            return mid
        if mid > start and arr[mid] < arr[mid-1]:
            end = mid - 1 
        if arr[start] <= arr[mid]:
            start = mid+1 
    return -1
def search(arr,target):
    pivot = pivot_fun(arr)
    if pivot == -1:
        return 0
    return pivot+1
    # print(f"The total no of array rotations is {pivot+1} which gives the rotation count for rotated sorted array")
    # if arr[pivot] == target:
    #     return pivot
    # if target > arr[0]:
    #     return binary_search(arr,target,0,pivot - 1)
    # return binary_search(arr,target,pivot+1,len(arr)-1)
res = search([4,5,6,7,0,1,2],0)
print(res)
