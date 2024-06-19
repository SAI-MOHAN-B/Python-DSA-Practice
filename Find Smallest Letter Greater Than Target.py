import math
class Solution:
    def nextGreatestLetter(self, arr: List[str], target: str) -> str:
        try:
            start = 0
            end = len(arr) - 1
            while start <= end:
                mid = math.floor(start + (end - start) / 2)
                if target > arr[mid]:
                    start = mid + 1
                elif target < arr[mid]:  
                    end = mid - 1
                else:
                    pass
        except Exception:
            return arr[0]
