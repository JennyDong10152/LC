class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        idx1 = self.search(nums, target, True)
        idx2 = self.search(nums, target, False)
        return [idx1, idx2]
    
    def search(self, nums, target, isFirst):
        left = 0
        right = len(nums)-1
        ans = -1

        while left <= right:
            mid = left + (right-left)//2
            midV = nums[mid]

            if midV == target:
                ans = mid
                if isFirst:
                    right = mid - 1
                else:
                    left = mid + 1
            elif midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return ans