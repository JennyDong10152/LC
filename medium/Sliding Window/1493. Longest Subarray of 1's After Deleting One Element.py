class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxLength = 0
        left = 0
        zeroes = 0

        for right, num in enumerate(nums):
            zeroes += not num
            while zeroes > 1:
                zeroes -= not nums[left]
                left += 1
            maxLength = max(maxLength, right - left)
        return maxLength