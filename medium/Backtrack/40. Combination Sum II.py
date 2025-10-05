class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates)
        self.answer = []
        self.backtrack(0, target, [])
        return self.answer
    
    def backtrack(self, start, target, temp):
        if not target:
            self.answer.append(list(temp))
            return 
        
        for idx in range(start, len(self.candidates)):
            if idx != start and self.candidates[idx] == self.candidates[idx-1]:
                continue
            if self.candidates[idx] > target:
                break
            temp.append(self.candidates[idx])
            self.backtrack(idx+1, target - self.candidates[idx], temp)
            temp.pop()