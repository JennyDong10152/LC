class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        count = 0
        prefix = defaultdict(int)
        prefixSum = 0
        prefix[0] = 1

        for num in nums:
            prefixSum += num
            count += prefix[prefixSum - goal]
            prefix[prefixSum] += 1
        return count