class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        currentSum = 0
        self.record = dict()
        return self.dynamic(nums, target, n, currentSum)
    
    def dynamic(self, nums, target, idx, currentSum):
        if (idx, currentSum) in self.record:
            return self.record[(idx, currentSum)]
        if idx < 0:
            if currentSum == target:
                return 1
            return 0

        positive = self.dynamic(nums, target, idx-1, currentSum + nums[idx])
        negative = self.dynamic(nums, target, idx-1, currentSum - nums[idx])
        self.record[(idx, currentSum)] = positive + negative
        return self.record[(idx, currentSum)]
