class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        self.dp = {}
        return self.search(k, n)
    
    def search(self, egg, floor):
        if egg == 1 or floor <= 1:
            return floor
        
        if (egg, floor) in self.dp:
            return self.dp[(egg, floor)]
        
        cnt = floor + 1
        broken = notBroken = 0
        left = 1
        right = floor

        while left <= right:
            mid = left + (right-left)//2
            broken = self.search(egg-1, mid-1)
            notBroken = self.search(egg, floor-mid)
            temp_cnt = 1 + max(broken, notBroken)

            if broken >= notBroken:
                right = mid - 1
            else:
                left = mid + 1
            cnt = min(temp_cnt, cnt)
        self.dp[(egg, floor)] = cnt
        return cnt