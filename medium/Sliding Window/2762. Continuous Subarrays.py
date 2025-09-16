class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        window = SortedList()
        left = 0
        count = 0

        for right, num in enumerate(nums):
            window.add(num)
            while window[-1] - window[0] > 2:
                window.remove(nums[left])
                left += 1
            count += right - left + 1
        return count