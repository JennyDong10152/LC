class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        count = 0
        window = SortedList()
        left = 0
        n = len(nums)

        for right in range(n):
            window.add(nums[right])
            while window[-1] - window[0] > 2:
                window.remove(nums[left])
                left += 1
            count += right - left + 1
        return count