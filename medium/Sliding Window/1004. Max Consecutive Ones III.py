class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        numZero = 0
        maxLength = 0

        for right, num in enumerate(nums):
            if not nums[right]:
                numZero += 1
            while numZero > k:
                numZero -= not nums[left]
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength