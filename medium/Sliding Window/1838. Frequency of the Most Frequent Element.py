class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = 0
        curSum = 0
        maxLength = 0

        for right, num in enumerate(nums):
            curSum += num
            while num * (right-left+1) - curSum > k:
                curSum -= nums[left]
                left += 1
            maxLength = max(maxLength, right-left+1)
        return maxLength