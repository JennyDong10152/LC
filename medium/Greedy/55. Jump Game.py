class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for idx, num in enumerate(nums):
            if idx > farthest:
                return False
            farthest = max(farthest, idx+num)
        return True