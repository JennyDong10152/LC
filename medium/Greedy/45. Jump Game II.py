class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        jumps = 0
        farthest = 0

        for idx, num in enumerate(nums):
            if end < idx:
                jumps += 1
                end = farthest
            farthest = max(farthest, idx+num)
        return jumps