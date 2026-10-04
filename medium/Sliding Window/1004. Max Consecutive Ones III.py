class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        maxLength = 0
        zero = 0
        left = 0

        for right, num in enumerate(nums):
            zero += not num
            while zero > k:
                zero -= not nums[left]
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength