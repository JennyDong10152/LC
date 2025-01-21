class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        record = defaultdict(int)
        left = 0
        maxLength = 0
        
        for right, char in enumerate(nums):
            record[char] += 1
            while record[char] > k:
                record[nums[left]] -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength