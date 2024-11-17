class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = len(nums)+1
        total = 0
        left = 0
        
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                size = min(size, i-left+1)
                total -= nums[left]
                left += 1
        return size if size != len(nums)+1 else 0