class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        self.nums = nums
        self.backtrack(0, [])
        return self.answer
    
    def backtrack(self, idx, temp):
        if idx == len(self.nums):
            self.answer.append(list(temp))
            return
        
        temp.append(self.nums[idx])
        self.backtrack(idx+1, temp)
        temp.pop()
        self.backtrack(idx+1, temp)