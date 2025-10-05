class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        self.visited = set()
        self.nums = sorted(nums)
        self.backtrack([])
        return self.answer
    
    def backtrack(self, temp):
        if len(temp) == len(self.nums):
            self.answer.append(list(temp))
            return
        
        for idx, num in enumerate(self.nums):
            if idx in self.visited:
                continue
            self.visited.add(idx)
            temp.append(num)
            self.backtrack(temp)
            temp.pop()
            self.visited.remove(idx)
