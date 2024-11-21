class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        if days == 1:
            return right
        if days == len(weights):
            return left
        
        while left <= right:
            mid = left + (right-left)//2
            days_needed = self.search(weights, mid)
            if days_needed > days:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def search(self, nums, target):
        cnt = 1
        temp_sum = 0
        for n in nums:
            if n + temp_sum > target:
                cnt += 1
                temp_sum = n
            else:
                temp_sum += n
        return cnt