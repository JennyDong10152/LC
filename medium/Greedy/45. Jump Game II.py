class Solution:
    def jump(self, nums: list[int]) -> int:
        count = 0
        farthest = 0
        end = 0

        for idx, num in enumerate(nums):
            if end < idx:
                count += 1
                end = farthest
            farthest = max(farthest, idx+num)
        return count