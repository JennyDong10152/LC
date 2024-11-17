class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        if days == 1:
            return right
            
        while left <= right:
            mid = left + (right-left)//2
            days_needed = self.count(weights, mid)
            if days_needed > days:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def count(self, weight, capacity):
        cnt = 1
        temp_sum = 0
        for w in weight:
            if w + temp_sum > capacity:
                cnt += 1
                temp_sum = w
            else:
                temp_sum += w
        return cnt
