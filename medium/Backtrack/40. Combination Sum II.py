class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates)
        self.answer = []
        self.find([], 0, target)
        return self.answer
    
    def find(self, temp, start, target):
        if target < 0:
            return
        if not target:
            self.answer.append(list(temp))
            return 
        
        for idx in range(start, len(self.candidates)):
            if idx > start and self.candidates[idx] == self.candidates[idx-1]:
                continue
            temp.append(self.candidates[idx])
            self.find(temp, idx+1, target - self.candidates[idx])
            temp.pop()