class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxLength = left = 0
        window = SortedList()
        n = len(nums)

        for right in range(n):
            window.add(nums[right])
            while window[-1] - window[0] > limit:
                window.remove(nums[left])
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength