class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        self.ans = []
        nums.sort()
        self.backtrack(nums, 0, [])
        return self.ans
    
    def backtrack(self, nums, idx, current):
        if idx == len(nums):
            self.ans.append(list(current))
            return
        
        current.append(nums[idx])
        self.backtrack(nums, idx+1, current)
        current.pop()

        while idx+1 < len(nums) and nums[idx] == nums[idx+1]:
            idx += 1
        self.backtrack(nums, idx+1, current)