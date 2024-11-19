class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        left = 0
        right = max(arr)
        min_diff = float("inf")
        ans = float("inf")

        while left <= right:
            mid = left + (right-left)//2
            temp_sum = sum(min(i, mid) for i in arr)
            temp_diff = abs(target-temp_sum)

            if temp_diff == min_diff:
                ans = min(mid, ans)
            if temp_diff < min_diff:
                ans = mid
                min_diff = temp_diff
            if not temp_diff:
                return mid
            
            if temp_sum >= target:
                right = mid - 1
            else:
                left = mid + 1
        return ans