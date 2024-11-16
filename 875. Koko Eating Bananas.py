class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right-left)//2
            hours = self.count(piles, mid) #num hours needed
            if hours > h:
                left = mid + 1
            else:
                right = mid
        return left
<<<<<<< Updated upstream

    def count(self, piles, target):
=======
    
    
    def count(self, piles, mid):
>>>>>>> Stashed changes
        cnt = 0
        
        for p in piles:
            if p%target != 0:
                cnt += 1
            cnt += p//target
        return cnt

        