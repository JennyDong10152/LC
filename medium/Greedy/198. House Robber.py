class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)

        for idx, num in enumerate(nums):
            dp[idx+1] = max(num+dp[idx-1], dp[idx])
        return dp[n]