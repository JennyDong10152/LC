class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [0] * (len(nums) + 1)

        for idx in range(len(nums)):
            dp[idx + 1] = max(nums[idx] + dp[idx-1], dp[idx])
        return dp[len(nums)]