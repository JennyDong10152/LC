class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = sum(piles)

        while left <= right:
            mid = left + (right-left)//2
            hours = self.search(piles, mid)
            if hours > h:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def search(self, piles, target):
        cnt = 0
        for p in piles:
            if p % target != 0:
                cnt += 1
            cnt += p // target
        return cnt