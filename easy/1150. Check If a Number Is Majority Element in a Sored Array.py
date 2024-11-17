class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        if not target in nums:
            return False
        
        idx1 = self.search(nums, target, True)
        idx2 = self.search(nums, target, False)
        return (idx2-idx1+1) > len(nums)/2
    
    def search(self, nums, target, isFirst):
        left = 0
        right = len(nums)-1
        idx = -1

        while left <= right:
            mid = left + (right-left)//2
            midV = nums[mid]
            if midV == target:
                idx = mid
                if isFirst:
                    right = mid - 1
                else:
                    left = mid + 1
            elif midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return idx