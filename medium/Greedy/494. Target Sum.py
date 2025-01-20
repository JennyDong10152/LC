class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        self.record = defaultdict(int)
        return self.find(nums, target, n, 0)
    
    def find(self, nums, target, idx, currentSum):
        if (idx, currentSum) in self.record:
            return self.record[(idx, currentSum)]
        if idx < 0:
            if currentSum == target:
                return 1
            return 0
        
        negative = self.find(nums, target, idx-1, currentSum - nums[idx])
        positive = self.find(nums, target, idx-1, currentSum + nums[idx])
        self.record[(idx, currentSum)] = positive + negative
        return self.record[(idx, currentSum)]