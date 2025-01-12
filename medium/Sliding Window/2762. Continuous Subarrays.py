class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        window = SortedList()
        left = 0
        total = 0

        for right in range(n):
            window.add(nums[right])
            while window[-1] - window[0] > 2:
                window.remove(nums[left])
                left += 1
            total += right - left + 1
        return tota