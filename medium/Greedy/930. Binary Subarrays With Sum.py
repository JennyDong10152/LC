class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        prefixSum = 0
        count = 0

        for idx, num in enumerate(nums):
            prefixSum += num
            count += prefix[prefixSum - goal]
            prefix[prefixSum] += 1

        return count