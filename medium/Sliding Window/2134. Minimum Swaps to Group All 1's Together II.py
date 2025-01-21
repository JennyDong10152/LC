class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        window = sum(nums)
        n = len(nums)
        swap = minSwap = nums[:window].count(0)

        for idx in range(window, n + window):
            swap -= not nums[(idx - window + n) % n]
            swap += not nums[idx % n]
            minSwap = min(minSwap, swap)
        return minSwap