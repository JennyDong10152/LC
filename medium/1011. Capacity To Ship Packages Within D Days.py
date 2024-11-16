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
    
    def count(self, weights, cap):
        cnt = 1
        total = 0
        for w in weights:
            if w > cap:
                return -1
            if total+w <= cap:
                total += w
            else:
                cnt += 1
                total = w
        return cnt
        