class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        minLength = len(nums) + 1
        if sum(nums) < target:
            return 0
        
        left = 0
        subsum = 0

        for right, num in enumerate(nums):
            subsum += num
            while subsum >= target:
                subsum -= nums[left]
                minLength = min(minLength, right - left + 1)
                left += 1
        return minLength