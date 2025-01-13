class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        n = len(nums)
        prefix = [0] * (n+1)
        for idx, num in enumerate(nums):
            prefix[idx+1] = prefix[idx] + num
        
        left = 0
        right = n-1
        while left <= right:
            mid = left + (right - left)//2
            if self.check(prefix, mid, target):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def check(self, prefix, idx, target):
        for i in range(idx, len(prefix)):
            if prefix[i] - prefix[i-idx] >= target:
                return True
        return False