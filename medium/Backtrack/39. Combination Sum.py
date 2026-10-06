class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
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