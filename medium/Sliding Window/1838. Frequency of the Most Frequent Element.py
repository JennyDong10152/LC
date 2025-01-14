class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = maxLength = subsum = 0

        for right, num in enumerate(nums):
            subsum += num
            while (nums[right] * (right-left+1))-subsum > k:
                subsum -= nums[left]
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength