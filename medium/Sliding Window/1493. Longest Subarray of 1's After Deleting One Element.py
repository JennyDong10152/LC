class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero = 0
        left = 0
        maxLength = 0

        for right, num in enumerate(nums):
            zero += not num
            while zero > 1:
                zero -= not nums[left]
                left += 1
            maxLength = max(maxLength, right - left)
        return maxLength