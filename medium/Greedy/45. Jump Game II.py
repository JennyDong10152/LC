class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        end = 0
        farthest = 0

        for idx, num in enumerate(nums[:-1]):
            farthest = max(farthest, idx + num)
            if idx == end:
                jumps += 1
                end = farthest
        return jumps