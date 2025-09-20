class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = sum(piles)

        while left <= right:
            mid = left + (right - left) // 2
            hours = self.count(piles, mid)
            if hours > h:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def count(self, piles, target):
        hours = 0
        for pile in piles:
            if pile % target:
                hours += 1
            hours += pile // target
        return hours