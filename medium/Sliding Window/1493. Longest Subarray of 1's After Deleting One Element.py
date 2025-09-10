class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxLength = 0
        left = 0
        zero = 0

        for right, num in enumerate(nums):
<<<<<<< Updated upstream
            if not num:
                zeroes += 1
            while zeroes > 1:
                zeroes -= not nums[left]
=======
            zero += not num
            while zero > 1:
                zero -= not nums[left]
>>>>>>> Stashed changes
                left += 1
            maxLength = max(maxLength, right - left)
        return maxLength
