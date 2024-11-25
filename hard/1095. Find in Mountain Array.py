# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        peak = self.findPeak(n, mountainArr)
        if mountainArr.get(peak) == target:
            return peak

        leftSearch = self.search(mountainArr, target, 0, peak-1, True)
        if leftSearch != -1:
            return leftSearch
        rightSearch = self.search(mountainArr, target, peak+1, n-1, False)
        return rightSearch
    
    def search(self, mountainArr, target, left, right, ascending):
        while left <= right:
            mid = left + (right-left)//2
            midV = mountainArr.get(mid)
            if midV == target:
                return mid
            elif midV > target:
                if ascending:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if ascending:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        

    def findPeak(self, n, mountainArr):
        left = 0
        right = n-1

        while left < right:
            mid = left + (right-left)//2
            midV = mountainArr.get(mid)
            if midV > mountainArr.get(mid+1):
                right = mid
            else:
                left = mid + 1
        return right
        