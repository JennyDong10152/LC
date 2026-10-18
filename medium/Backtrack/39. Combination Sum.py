class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
<<<<<<< Updated upstream
        self.ans = []
        self.target = target
        self.candidates = sorted(candidates)
        self.backtrack(0, 0, [])
        return self.ans
    
    def backtrack(self, idx, curSum, curCombo):
        if self.target == curSum:
            self.ans.append(list(curCombo))
            return
        if self.target < curSum:
            return
        
        for i in range(idx, len(self.candidates)):
            curCombo.append(self.candidates[i])
            self.backtrack(i, curSum + self.candidates[i], curCombo)
            curCombo.pop()
=======
        self.candidates = sorted(candidates)
        self.ans = []
        self.backtrack(target, 0, [])
        return self.ans

    def backtrack(self, target, start, current):
        if target == sum(current):
            self.ans.append(list(current))
            return
        
        if target < sum(current):
            return 

        for idx in range(start, len(self.candidates)):
            current.append(self.candidates[idx])
            self.backtrack(target, idx, current)
            current.pop()
>>>>>>> Stashed changes
