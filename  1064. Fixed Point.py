class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)-1
        ans = -1

        while left <= right:
            mid = left + (right-left)//2
            midV = arr[mid]
            if midV == mid:
                ans = mid
            if midV >= mid:
                right = mid - 1
            else:
                left = mid + 1
        return ans