class Solution:
    def jump(self, nums: list[int]) -> int:
        farthest = 0
        endpoint = 0
        jump = 0

        for idx, num in enumerate(nums):
            if endpoint < idx:
                endpoint = farthest
                jump += 1
            farthest = max(farthest, idx + num)
        return jump