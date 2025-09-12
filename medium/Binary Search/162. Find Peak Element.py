class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right-left) // 2
            midV = nums[mid]
            if midV > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return right