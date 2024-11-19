import random

class Solution:
    def __init__(self, w: list[int]):
        self.prefix = []
        curr_sum = 0
        for weight in w:
            curr_sum += weight
            self.prefix.append(curr_sum)
        self.total = curr_sum

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        
        left = 0
        right = len(self.prefix) - 1

        while left < right:
            mid = (left + right) // 2
            midV = self.prefix[mid]
            if midV >= target:
                right = mid
            else:
                left = mid + 1
        return left
