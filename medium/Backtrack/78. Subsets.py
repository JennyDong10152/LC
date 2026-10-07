class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.ans = []
        self.backtrack(nums, 0, [])
        return self.ans
    
    def backtrack(self, nums, idx, current):
        if idx == len(nums):
            self.ans.append(list(current))
            return
        
        current.append(nums[idx])
        self.backtrack(nums, idx+1, current)
        current.pop()
        self.backtrack(nums, idx+1, current)