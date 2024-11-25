class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        n = len(nums)
        left = 0
        right = n-1

        prefix = [0] * (n+1)
        for i, n in enumerate(nums):
            prefix[i+1] = prefix[i] + n 

        while left <= right:
            mid = left + (right-left)//2
            if self.search(prefix, mid, target):
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def search(self, prefix, length, target):
        for i in range(length, len(prefix)):
            if prefix[i]-prefix[i-length] >= target:
                return True
        return False