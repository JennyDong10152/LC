class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxLength = 0
        left = 0
        zero = 0

        for right, num in enumerate(nums):
            zeroes += not num
            while zero > 1:
                zero -= not nums[left]
                left += 1
            maxLength = max(maxLength, right - left)
        return maxLength
