class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = left + (right - left) // 2
            day_needed = self.count(weights, mid)
            if day_needed > days:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def count(self, weights, target):
        day = 1
        curW = 0
        for w in weights:
            if curW + w > target:
                day += 1
                curW = 0
            curW += w
        return day
