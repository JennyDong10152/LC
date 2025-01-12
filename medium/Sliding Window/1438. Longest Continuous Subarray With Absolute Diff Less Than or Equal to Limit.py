class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        window = SortedList()
        left = maxLength = 0

        for right in range(n):
            window.add(nums[right])
            if window[-1] - window[0] > limit:
                window.remove(nums[left])
                left += 1
            maxLength = max(maxLength, right-left+1)
        return maxLength
