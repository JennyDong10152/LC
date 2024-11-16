class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        left = 0
        right = max(arr)
        min_diff = float('inf')
        ans = 0

        while left <= right:
            mid = left + (right-left)//2
<<<<<<< Updated upstream
            temp_sum = sum(min(i, mid) for i in arr)
            cur_diff = abs(target-temp_sum)
=======
            temp_sum = sum(min(mid, i) for i in arr)
            cur_diff = abs(target - temp_sum)

>>>>>>> Stashed changes
            if not cur_diff:
                return mid
            if cur_diff == min_diff:
                ans = min(ans, mid)
            elif cur_diff < min_diff:
                min_diff = cur_diff
                ans = mid
<<<<<<< Updated upstream
            
=======
                
>>>>>>> Stashed changes
            if temp_sum > target:
                right = mid - 1
            else:
                left = mid + 1
        return ans
            