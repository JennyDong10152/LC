import random
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix = []
        curr = 0
        for a, b, x, y in rects:
            curr += ((x-a+1)*(y-b+1))
            self.prefix.append(curr)
        self.total = curr

    def pick(self) -> List[int]:
        target = random.randint(1, self.total)
        idx = self.search(target)
        a, b, x, y = self.rects[idx]
        u = random.randint(a, x)
        v = random.randint(b, y)
        return [u,v]

    def search(self, target):
        left = 0
        right = len(self.rects)-1
        while left < right:
            mid = left + (right - left)//2
            midV = self.prefix[mid]
            if midV >= target:
                right = mid
            else:
                left = mid + 1
        return left