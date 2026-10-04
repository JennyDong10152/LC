class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        self.record = defaultdict(int)
        return self.find(nums, target, 0, 0)
        
    def find(self, nums, target, idx, current):
        if idx == len(nums):
            return 1 if current == target else 0
        if (idx, current) in self.record:
            return self.record[(idx, current)]
        
        add = self.find(nums, target, idx+1, current+nums[idx])
        sub = self.find(nums, target, idx+1, current-nums[idx])

        self.record[(idx, current)] = add+sub
        return self.record[(idx, current)]