class Solution:
    def jump(self, nums: list[int]) -> int:
        farthest = 0
        jump = 0
        endpoint = 0

        for idx, num in enumerate(nums):
            if idx > endpoint:
                jump += 1
                endpoint = farthest
            farthest = max(farthest, idx + num)
        return jump