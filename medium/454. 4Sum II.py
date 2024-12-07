class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        freq_firstTwoSum = defaultdict(int)
        freq_lastTwoSum = defaultdict(int)
        cnt = 0

        for i in range(len(nums1)):
            for j in range(len(nums1)):
                freq_firstTwoSum[nums1[i]+nums2[j]] += 1
                freq_lastTwoSum[nums3[i]+nums4[j]] += 1
        firstTwoSum = sorted(list(freq_firstTwoSum))        
        lastTwoSum = sorted(list(freq_lastTwoSum))

        for sum1 in firstTwoSum:
            founded = self.search(lastTwoSum, sum1)
            if founded:
                cnt += (freq_firstTwoSum[sum1] * freq_lastTwoSum[-sum1])
        return cnt
    
    def search(self, nums, target):
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left + (right-left)//2
            midV = nums[mid] + target
            if not midV:
                return True
            elif midV > 0:
                right = mid - 1
            else:
                left = mid + 1
        return False
