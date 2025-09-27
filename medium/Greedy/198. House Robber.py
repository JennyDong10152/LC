class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        for idx, num in enumerate(nums):
            dp[idx+1] = max(dp[idx], dp[idx-1] + num)
        return dp[len(nums)]