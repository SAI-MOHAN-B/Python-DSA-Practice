import math


def binary_search(arr, target, start, end):
    while start <= end:
        mid = math.floor(start + (end - start) / 2)
        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            return mid
    return -1


def ans(arr, target):
    start = 0
    end = 1
    # condition to check whether the target element is greater than end
    while target > arr[end]:
        # new start
        temp = end + 1
        # double the box value
        # end = previous end + sizeofbox * 2
        end = end + (end - start + 1) * 2
        start = temp
    return binary_search(arr, target, start, end)


# Driver function
arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
res = ans(arr, 10)
if ans == -1:
    print("Element not found")
else:
    print("Element found at index", res)
