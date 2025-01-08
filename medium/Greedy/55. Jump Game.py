class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current = 0
        for idx, num in enumerate(nums):
            if idx > current:
                return False
            current = max(current, idx+num)
        return True