class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        freq_firstTwoSum = {}
        freq_lastTwoSum = {}

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                freq_firstTwoSum[nums1[i]+nums2[j]] = freq_firstTwoSum.get(nums1[i]+nums2[j], 0)+1
                freq_lastTwoSum[nums3[i]+nums4[j]] = freq_lastTwoSum.get(nums3[i]+nums4[j], 0)+1
        firstTwoSum = sorted(list(freq_firstTwoSum))
        lastTwoSum = sorted(list(freq_lastTwoSum))
        cnt = 0
        for sum1 in firstTwoSum:
            sum2 = self.search(sum1, lastTwoSum)
            if sum2 is None:
                continue
            else:
                cnt += (freq_firstTwoSum[sum1] * freq_lastTwoSum[sum2])
        return cnt

    def search(self, sum1, nums):
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left + (right-left)//2
            midV = nums[mid]
            if midV + sum1 == 0:
                return midV
            elif midV + sum1 > 0:
                right = mid-1
            else:
                left = mid+1
        return None
    
