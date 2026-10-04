class Solution:
    def maxJump(self, stones: list[int]) -> int:
        n = len(stones)
        ans = stones[1]

        for idx in range(n-2):
            ans = max(ans, stones[idx+2] - stones[idx])
        return ans