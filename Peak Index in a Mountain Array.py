import math
# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# https://leetcode.com/problems/find-peak-element/
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
            start = 0
            end = len(arr) - 1
            while start < end:
                mid = math.floor((start + (end - start) / 2))
                # you are in dec part of array
                # this may be the ans, but look at left
                # this is why end != mid - 1
                if arr[mid] > arr[mid+1]:
                    end = mid
                else:
                    start = mid + 1
            return start
 # in the end, start == end and pointing to the largest number because of the 2 checks above
 #  start and end are always trying to find max element in the above 2 checks
 #  hence, when they are pointing to just one element, that is the max one because that is what the checks say
 #  more elaboration: at every point of time for start and end, they have the best possible answer till that time
 #  and if we are saying that only one item is remaining, hence cuz of above line that is the best possible ans
 #  return start; // or return end as both are =
