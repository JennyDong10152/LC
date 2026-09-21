class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        jumps = 0
        end = 0

        for idx, num in enumerate(nums):
            if idx > end:
                jumps += 1
                end = farthest
            farthest = max(farthest, idx + num)
        return jumps