class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = left + (right - left) // 2
            day = self.count(weights, mid)
            if day > days:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def count(self, weights, target):
        day = 1
        currentSum = 0
        for weight in weights:
            if currentSum + weight > target:
                day += 1
                currentSum = 0
            currentSum += weight
        return day