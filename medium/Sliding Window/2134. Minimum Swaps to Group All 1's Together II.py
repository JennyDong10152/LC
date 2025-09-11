class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        window = sum(nums)
        swap = minSwap = nums[:window].count(0)
        n = len(nums)

        for idx in range(window, window+n):
            swap -= not nums[(idx-window) % n]
            swap += not nums[idx % n]
            minSwap = min(minSwap, swap)
        return minSwap