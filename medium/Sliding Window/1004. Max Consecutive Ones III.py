class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxLength = 0
        zeroCount = 0

        for right in range(len(nums)):
            if not nums[right]:
                zeroCount += 1
            while zeroCount > k:
                if not nums[left]:
                    zeroCount -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength