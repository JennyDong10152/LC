class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxFrequency = 0
        left = 0
        subsum = 0

        for right, num in enumerate(nums):
            subsum += num
            while (right-left+1) * num - subsum > k:
                subsum -= nums[left]
                left += 1
            maxFrequency = max(maxFrequency, right - left + 1)
        return maxFrequency