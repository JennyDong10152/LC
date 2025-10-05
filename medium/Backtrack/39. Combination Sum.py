class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = []
        self.candidates = sorted(candidates)
        self.backtrack(0, target, [])
        return self.answer
    
    def backtrack(self, start, target, temp):
        if not target:
            self.answer.append(list(temp))
            return
        
        for idx in range(start, len(self.candidates)):
            if self.candidates[idx] > target:
                break
            temp.append(self.candidates[idx])
            self.backtrack(idx, target - self.candidates[idx], temp)
            temp.pop()
