class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = left + (right - left) // 2
            canShip = self.calculate(weights, days, mid)
            if canShip:
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def calculate(self, weights, days, capacity):
        count = 1
        temp = 0
        for weight in weights:
            temp += weight
            if temp > capacity:
                count += 1
                temp = weight
        return True if count <= days else False
            