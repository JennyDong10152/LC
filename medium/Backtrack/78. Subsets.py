class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subset = []
        self.n = len(nums)
        self.backtrack(0, [], nums)
        return self.subset
    
    def backtrack(self, start, temp, nums):
        if start == self.n:
            self.subset.append(list(temp))
            return
        temp.append(nums[start])
        self.backtrack(start+1, temp, nums)
        temp.pop()
        self.backtrack(start+1, temp, nums)