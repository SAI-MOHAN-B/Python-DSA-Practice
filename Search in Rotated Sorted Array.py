import math
from typing import List

class Solution:
    def binary_search(self, arr: List[int], target: int, start: int, end: int) -> int:
        while start <= end:
            mid = math.floor(start + (end - start) / 2)
            if target == arr[mid]:
                return mid
            if target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def search(self, arr: List[int], target: int) -> int:
        # find the pivot element
        pivot = self.find_pivot(arr)
        # if you didn't find out the pivot element then
        if pivot == -1:
            return self.binary_search(arr, target, 0, len(arr) - 1)
        # if pivot is found you have found out  2 asc sorted arrays
        if arr[pivot] == target:
            return pivot
        # if the target is greater than start
        # search starting from 0, till pivot - 1
        # because the elements after pivot will be smaller
        if target >= arr[0]:
            return self.binary_search(arr, target, 0, pivot - 1)
        # if the target is lesser than start
        # search starting from pivot + 1, till end
        # because the elements after pivot will be smaller
        # as well as we know that elements from start to pivot
        # are going to be bigger than target
        return self.binary_search(arr, target, pivot + 1, len(arr) - 1)

    def find_pivot(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = math.floor(start + (end - start) / 2)
            # suppose if the array exceeds the end 
            # it reaches the end of the array 
            # then it will throws an exception
            # so we need to check whether the mid is within end
            # or it is lesser than array
            if mid < end and arr[mid] > arr[mid + 1]:
                return mid
            # suppose if the pivot lies in the left part of the array
            # so mid should always be greater than start
            # if it goes left side then array index out of bound exception
            if mid > start and arr[mid] < arr[mid - 1]:
                return mid - 1
            if arr[mid] <= arr[start]:
                end = mid - 1
            else:
                start = mid + 1
        return -1
