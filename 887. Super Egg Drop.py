class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        self.dp = {}
        return self.search(k, n)
    
    def search(self, egg, floor):
        if floor <= 1 or egg == 1:
            return floor

        if (egg, floor) in self.dp:
            return self.dp[(egg, floor)]
        
        broken = notBroken = 0
        left = 1
        right = floor
        cnt = floor+1

        while left <= right:
            mid = left + (right-left)//2
            #if broken, egg -= 1, need to check floors below mid
            broken = self.search(egg-1,mid-1)
            notBroken = self.search(egg, floor-mid)
            temp_cnt = 1 + max(broken, notBroken)

            if broken >= notBroken:
                right = mid - 1
            else:
                left = mid + 1
            cnt = min(cnt, temp_cnt)
        self.dp[(egg, floor)] = cnt
        return cnt
