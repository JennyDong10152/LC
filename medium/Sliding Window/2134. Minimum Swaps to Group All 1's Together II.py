class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        window = sum(nums)
        swap = minSwap = nums[:window].count(0)

        for idx in range(window, len(nums)+window):
            swap -= not nums[(idx-window) % len(nums)]
            swap += not nums[idx % len(nums)]
            minSwap = min(minSwap, swap)
        return minSwap