class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
<<<<<<< Updated upstream
        self.ans = []
        self.backtrack(sorted(nums), 0, [], set())
        return self.ans

    def backtrack(self, nums, start, curCombo, visited):
        if len(curCombo) == len(nums):
            self.ans.append(list(curCombo))
            return
        
        for idx in range(len(nums)):
            if nums[idx] in visited:
                continue
            visited.add(nums[idx])
            curCombo.append(nums[idx])
            self.backtrack(nums, idx+1, curCombo, visited)
            visited.remove(nums[idx])
            curCombo.pop()
=======
        self.visited = set()
        self.ans = []
        self.backtrack(nums, [])
        return self.ans
        
    def backtrack(self, nums, current):
        if len(current) == len(nums):
            self.ans.append(list(current))
            return
        
        for idx, num in enumerate(nums):
            if num not in self.visited:
                self.visited.add(num)
                current.append(num)
                self.backtrack(nums, current)
                current.pop()
                self.visited.remove(num)
>>>>>>> Stashed changes
