class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        left = 0
        right = max(arr)
        min_diff = float('inf')
        ans = -1

        while left <= right:
            mid = left + (right-left)//2
            temp_sum = sum(min(i, mid) for i in arr)
            curr_diff = abs(target - temp_sum)

            if curr_diff == min_diff:
                ans = min(ans, mid)
            if curr_diff < min_diff:
                ans = mid
                min_diff = curr_diff

            if not min_diff:
                return ans
            if temp_sum > target:
                right = mid - 1
            else:
                left = mid + 1
        return ans