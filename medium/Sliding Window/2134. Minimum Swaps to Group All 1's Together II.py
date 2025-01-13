class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        window = sum(nums)
        n = len(nums)
        swap = minSwap = nums[:window].count(0)

        for idx in range(window, window + n):
            swap += not nums[idx % n]
            swap -= not nums[(idx - window + n) % n]
            minSwap = min(minSwap, swap)
        return minSwap