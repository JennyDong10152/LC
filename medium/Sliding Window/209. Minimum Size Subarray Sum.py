class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        minLength = len(nums)
        subsum = 0
        left = 0
        
        for right, num in enumerate(nums):
            subsum += num
            while subsum >= target:
                minLength = min(minLength, right-left+1)
                subsum -= nums[left]
                left += 1
        return minLength