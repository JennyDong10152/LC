class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        self.nums = sorted(nums)
        self.visited = set()
        self.search([])
        return self.answer
    
    def search(self, temp):
        if len(temp) == len(self.nums):
            self.answer.append(list(temp))
            return
        
        for idx in range(len(self.nums)):
            if idx in self.visited:
                continue
            self.visited.add(idx)
            temp.append(self.nums[idx])
            self.search(temp)
            self.visited.remove(idx)
            temp.pop()