class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        window = sum(nums)
        minLength = count = nums[:window].count(0)
        n = len(nums)

        for i in range(window, n + window):
            count += not nums[i % n]
            count -= not nums[(i - window + n) % n]
            minLength = min(minLength, count)
        return minLength