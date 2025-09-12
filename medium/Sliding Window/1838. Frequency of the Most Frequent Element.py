class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        subsum = 0
        left = 0
        maxFrequency = 0

        for right, num in enumerate(nums):
            subsum += num
            while num * (right-left+1) - subsum > k:
                subsum -= nums[left]
                left += 1
            maxFrequency = max(maxFrequency, right-left+1)
        return maxFrequency