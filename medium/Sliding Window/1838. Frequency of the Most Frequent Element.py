class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        subsum = 0
        frequency = 0
        left = 0

        for right, num in enumerate(nums):
            subsum += num
            while (right - left + 1) * num - subsum > k:
                subsum -= nums[left]
                left += 1
            frequency = max(frequency, right - left + 1)
        return frequency