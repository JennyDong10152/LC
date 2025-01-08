class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        answer = stones[1]
        for idx in range(n-2):
            answer = max(answer, stones[idx+2]-stones[idx])
        return answer