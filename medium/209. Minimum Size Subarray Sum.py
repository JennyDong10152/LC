class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        n = len(nums)
        prefix = [0] * (n+1)
        for i, n in enumerate(nums):
            prefix[i+1] = prefix[i] + n

        left = 0
        right = len(nums)

        while left <= right:
            mid = left + (right-left)//2
            if self.check(prefix, mid, target):
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def check(self, prefix, length, target):
        for idx in range(length, len(prefix)):
            if prefix[idx] - prefix[idx-length] >= target:
                return True
        return False