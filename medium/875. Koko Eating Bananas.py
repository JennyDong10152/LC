class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        if h == 1:
            return right
        
        while left <= right:
            mid = left + (right-left)//2
            hours = self.count(piles, mid)
            if hours > h:
                left = mid + 1
            else:
                right = mid - 1
        return left

    
    def count(self, piles, target):
        cnt = 0
        for p in piles:
            if p % target:
                cnt += 1
            cnt += (p//target)
        return cnt