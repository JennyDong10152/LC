class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates)
        self.answer = []
        self.find(0, [], target)
        return self.answer
    
    def find(self, start, temp, target):
        if target < 0:
            return
        if not target:
            self.answer.append(list(temp))
            return 
        
        for idx in range(start, len(self.candidates)):
            if self.candidates[idx] > target:
                break
            temp.append(self.candidates[idx])
            self.find(idx, temp, target - self.candidates[idx])
            temp.pop()