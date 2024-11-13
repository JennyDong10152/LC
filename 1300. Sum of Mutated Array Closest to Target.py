class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        if sum(arr) == target:
            return max(arr)
        
        left = 0
        ans = 0
        right = max(arr)

        min_dif = float('inf')
        
        while left <= right:
            mid = left + (right-left)//2
            temp_sum = sum(min(i, mid) for i in arr)

            cur_dif = abs(target-temp_sum)
            if not cur_dif:
                return mid

            if cur_dif == min_dif:
                ans = min(ans, mid)
                
            elif cur_dif < min_dif:
                min_dif = cur_dif
                ans = mid

            if temp_sum > target:
                right = mid - 1
            else:
                left = mid + 1
        return ans

