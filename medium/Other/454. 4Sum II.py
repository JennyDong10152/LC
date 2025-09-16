class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        freq_firstTwoSum = defaultdict(int)
        freq_lastTwoSum = defaultdict(int)
        count = 0

        for i in range(len(nums1)):
            for j in range(len(nums1)):
                freq_firstTwoSum[nums1[i]+nums2[j]] += 1
                freq_lastTwoSum[nums3[i]+nums4[j]] += 1
        firstTwoSum = sorted(list(freq_firstTwoSum))
        lastTwoSum = sorted(list(freq_lastTwoSum))

        for sum1 in firstTwoSum:
            exists = freq_lastTwoSum[-sum1]
            if exists:
                count += (freq_firstTwoSum[sum1] * freq_lastTwoSum[-sum1])
        return count