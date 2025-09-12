class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxLength = 0
        zeroes = 0

        for right, num in enumerate(nums):
            zeroes += not num
            while zeroes > k:
                zeroes -= not nums[left]
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength