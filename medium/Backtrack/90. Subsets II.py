class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.subsets = set()
        self.n = len(nums)
        self.backtrack(sorted(nums), 0, [])
        return list(self.subsets)

    def backtrack(self, nums, idx, temp):
        if idx == self.n:
            self.subsets.add(tuple(temp))
            return 
        temp.append(nums[idx])
        self.backtrack(nums, idx+1, temp)
        temp.pop()
        self.backtrack(nums, idx+1, temp)