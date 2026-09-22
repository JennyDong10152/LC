class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        self.record = defaultdict(int)
        return self.find(nums, target, 0, 0)

    def find(self, nums, target, idx, currentSum):
        if idx == len(nums):
            return 1 if currentSum == target else 0
        if (idx, currentSum) in self.record:
            return self.record[(idx, currentSum)]
        
        add = self.find(nums, target, idx+1, currentSum + nums[idx])
        sub = self.find(nums, target, idx+1, currentSum - nums[idx])

        self.record[(idx, currentSum)] = add + sub
        return self.record[(idx, currentSum)]
