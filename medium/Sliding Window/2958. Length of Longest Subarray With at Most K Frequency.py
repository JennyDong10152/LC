class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        frequency = defaultdict(int)
        left = 0
        maxLength = 0

        for right, num in enumerate(nums):
            frequency[num] += 1
            while frequency[num] > k:
                frequency[nums[left]] -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength