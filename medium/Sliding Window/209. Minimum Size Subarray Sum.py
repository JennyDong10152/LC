class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        minLength = len(nums) + 1
        left = 0
        curSum = 0

        for right, num in enumerate(nums):
            curSum += num
            while curSum >= target:
                curSum -= nums[left]
                minLength = min(minLength, right - left + 1)
                left += 1
        return minLength if minLength != len(nums) + 1 else 0