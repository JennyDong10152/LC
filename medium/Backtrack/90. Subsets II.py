class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.answer = set()
        self.nums = sorted(nums)
        self.backtrack(0, [])
        return list(self.answer)
    
    def backtrack(self, idx, temp):
        if idx == len(self.nums):
            self.answer.add(tuple(temp))
            return
        
        temp.append(self.nums[idx])
        self.backtrack(idx+1, temp)
        temp.pop()
        self.backtrack(idx+1, temp)