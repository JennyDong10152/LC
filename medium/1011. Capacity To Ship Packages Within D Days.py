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
            days_needed = self.count(weights, mid)
            if days_needed > days:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def count(self, weights, target):
        cnt = 1
        cur_sum = 0

        for w in weights:
            if w+cur_sum > target:
                cnt += 1
                cur_sum = w
            else:
                cur_sum += w
        return cnt