import random
class Solution:

    def __init__(self, w: List[int]):
        self.total = 0
        cur_sum = 0
        self.prefix = []

        for weight in w:
            cur_sum += weight
            self.prefix.append(cur_sum)
        self.total = cur_sum

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        left = 0
        right = len(self.prefix)

        while left < right:
            mid = left + (right-left)//2
            midV = self.prefix[mid]
            if midV >= target:
                right = mid
            else:
                left = mid + 1
        return left