class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        maxLength = 0
        left = 0
        subsum = 0

        for right, num in enumerate(nums):
            subsum += num
            while (right - left + 1) * num - subsum > k:
                subsum -= nums[left]
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength