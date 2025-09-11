class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        maxLength = 0
        frequency = defaultdict(int)

        for right, num in enumerate(nums):
            frequency[num] += 1
            while frequency[num] > k:
                frequency[nums[left]] -= 1
                if not frequency[nums[left]]:
                    del frequency[nums[left]]
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength