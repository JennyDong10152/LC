class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        self.nums = sorted(nums)
        self.visited = set()
        self.search([])
        return self.answer
    
    def search(self, temp):
        if len(temp) == len(self.nums):
            self.answer.append(temp)
            return 
            
        for idx in range(len(self.nums)):
            if idx in self.visited:
                continue
            self.visited.add(idx)
            self.search(temp+[self.nums[idx]])
            self.visited.remove(idx)