class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxLength = 0
        left = 0
        zeroes = 0

        for right, num in enumerate(nums):
            if not num:
                zeroes += 1
            while zeroes > 1:
                zeroes -= not nums[left]
                left += 1
            maxLength = max(maxLength, right - left)
        return maxLength