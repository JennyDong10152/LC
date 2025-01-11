class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSum = 0
        prefixMap = {0 : 1}
        count = 0

        for num in nums:
            prefixSum += num
            mod = prefixSum % k
            if mod < 0:
                mod = -mod
            if mod in prefixMap:
                count += prefixMap[mod]
                prefixMap[mod] += 1
            else:
                prefixMap[mod] = 1
        return count