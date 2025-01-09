class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = left + (right-left)//2
            days_needed = self.count(weights, mid)
            if days_needed > days:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def count(self, weights, target):
        day = 1
        capacity = 0
        for weight in weights:
            if capacity + weight > target:
                day += 1
                capacity = weight
            else:
                capacity += weight
        return day 