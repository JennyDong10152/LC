class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
            if self.candidates[idx] > target:
                break
            self.search(target-self.candidates[idx], idx, combo+[self.candidates[idx]])