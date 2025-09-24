class Solution:

    def __init__(self, w: List[int]):
        curr = 0
        self.prefix = []
        for weight in w:
            curr += weight
            self.prefix.append(curr)
        self.total = curr

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        idx = self.search(target)
        return idx
    
    def search(self, target):
        left = 0
        right = len(self.prefix) - 1

        while left < right:
            mid = left + (right - left) // 2
            midV = self.prefix[mid]
            if midV >= target:
                right = mid
            else:
                left = mid + 1
        return left

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()