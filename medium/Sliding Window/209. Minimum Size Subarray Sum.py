class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        minArray = len(nums)+1
        if sum(nums) < target:
            return 0

        left = 0
        subsum = 0

        for right, num in enumerate(nums):
            subsum += num
            while subsum >= target:
                subsum -= nums[left]
                minArray = min(minArray, right - left + 1)
                left += 1
        return minArray