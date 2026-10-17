class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        self.candidates = sorted(candidates)
        self.ans = []
<<<<<<< Updated upstream
        self.target = target
        self.backtrack(0, 0, [])
        return self.ans
    
    def backtrack(self, curidx, curSum, curCombo):
        if curSum == self.target:
            self.ans.append(list(curCombo))
=======
        self.backtrack(0, target, [])
        return self.ans
    
    def backtrack(self, start, target, current):
        if sum(current) == target:
            self.ans.append(list(current))
            return
        
        if sum(current) > target:
>>>>>>> Stashed changes
            return
        
        if curSum > self.target:
            return
        
        for idx in range(curidx, len(self.candidates)):
            if idx > curidx and self.candidates[idx] == self.candidates[idx - 1]:
                continue
<<<<<<< Updated upstream
            curCombo.append(self.candidates[idx])
            self.backtrack(idx+1, curSum + self.candidates[idx], curCombo)
            curCombo.pop()
=======
            current.append(self.candidates[idx])
            self.backtrack(idx+1, target, current)
>>>>>>> Stashed changes
