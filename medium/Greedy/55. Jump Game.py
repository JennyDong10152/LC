class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest = 0

        for idx, num in enumerate(nums):
            if farthest < idx:
                return False
            farthest = max(farthest, idx + num)
        return True