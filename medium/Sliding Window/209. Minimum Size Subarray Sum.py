class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        minLength = len(nums)+1
        curSum = 0
        left = 0

        for right, num in enumerate(nums):
            curSum += num
            while curSum >= target:
                minLength = min(minLength, right-left+1)
                curSum -= nums[left]
                left += 1
        return minLength if minLength != len(nums)+1 else 0