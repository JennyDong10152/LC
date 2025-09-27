class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1

        for current in range(target+1):
            for num in nums:
                if current - num >= 0:
                    dp[current] += dp[current-num]
                else:
                    break
        return dp[target]