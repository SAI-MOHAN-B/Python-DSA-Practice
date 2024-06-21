import math
class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        def search(arr,target,findstartindex):
            start = 0
            end = len(arr) - 1
            ans = -1
            while start<=end:
                mid = math.floor(start+(end-start)/2)
                if target<arr[mid]:
                    end = mid - 1
                elif target>arr[mid]:
                    start = mid + 1
                else:
                    ans = mid
                    if findstartindex:
                        end = mid - 1
                    else:
                        start = mid + 1
            return ans
        temp = [-1,-1]
        start = search(arr,target,True)
        end = search(arr,target,False)
        temp[0] = start
        temp[1] = end
        return temp



