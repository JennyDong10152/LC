import random
class Solution:

    def __init__(self, w: List[int]):
        cur = 0
        self.prefix = []
        for weight in w:
            cur += weight
            self.prefix.append(cur)
        self.total = cur

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        idx = self.search(target)
        return idx
    
    def search(self, target):
        left = 0
        right = len(self.prefix)-1
        while left < right:
            mid = left + (right-left)//2
            midV = self.prefix[mid]
            if midV >= target:
                right = mid
            else:
                left = mid + 1
        return left