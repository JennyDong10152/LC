class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        left = 0
        right = max(arr)
        ans = right + 1
        minDiff = float("inf")

        while left <= right:
            mid = left + (right - left) // 2
            tempSum = sum(min(num, mid) for num in arr)
            tempDiff = abs(tempSum - target)
            if not tempDiff:
                return mid
            
            if tempDiff == minDiff:
                ans = min(mid, ans)
            if tempDiff < minDiff:
                ans = mid
                minDiff = tempDiff
            
            if tempSum > target:
                right = mid - 1
            else:
                left = mid + 1
        return ans