class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxZero = 0
        maxLength = 0

        for right, num in enumerate(nums):
            maxZero += not num
            while maxZero > k:
                maxZero -= not nums[left]
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength