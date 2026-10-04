class Solution:
    def jump(self, nums: list[int]) -> int:
        farthest = 0
        end = 0
        count = 0

        for idx, num in enumerate(nums):
            if end < idx:
                end = farthest
                count += 1
            farthest = max(farthest, idx+num)
        return count