class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = sum(piles)

        while left < right:
            mid = left + (right - left) // 2
            hour = self.eat(piles, mid)
            if hour > h:
                left = mid + 1
            else:
                right = mid
        return left

    def eat(self, piles, rate):
        count = 0
        for p in piles:
            count += p // rate
            count += 1 if p % rate else 0
        return count