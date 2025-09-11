class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        window = SortedList()
        maxLength = 0
        left = 0

        for right, num in enumerate(nums):
            window.add(num)
            while window[-1] - window[0] > limit:
                window.remove(nums[left])
                left += 1
            maxLength = max(maxLength, right-left+1)
        return maxLength