class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = sum(piles)

        while left <= right:
            mid = left + (right - left) // 2
            hour = self.eat(piles, mid)
            if hour > h:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def eat(self, piles, target):
        hour = 0
        for p in piles:
            hour += p//target
            hour += 1 if p%target else 0
        return hour