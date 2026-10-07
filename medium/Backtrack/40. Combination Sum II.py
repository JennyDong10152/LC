class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        self.candidates = sorted(candidates)
        self.ans = []
        self.target = target
        self.backtrack(0, 0, [])
        return self.ans
    
    def backtrack(self, curidx, curSum, curCombo):
        if curSum == self.target:
            self.ans.append(list(curCombo))
            return
        
        if curSum > self.target:
            return
        
        for idx in range(curidx, len(self.candidates)):
            if idx > curidx and self.candidates[idx] == self.candidates[idx - 1]:
                continue
            curCombo.append(self.candidates[idx])
            self.backtrack(idx+1, curSum + self.candidates[idx], curCombo)
            curCombo.pop()
