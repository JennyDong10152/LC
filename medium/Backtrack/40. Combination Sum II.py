class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates)
        self.sums = []
        self.search(target, 0, [])
        return self.sums
    
    def search(self, target, start, combo):
        if target < 0:
            return
        if target == 0:
            self.sums.append(combo)
            return 
        for idx in range(start, len(self.candidates)):
            if idx > start and self.candidates[idx] == self.candidates[idx-1]:
                continue
            if self.candidates[idx] > target:
                break
            self.search(target-self.candidates[idx], idx+1, combo+[self.candidates[idx]])