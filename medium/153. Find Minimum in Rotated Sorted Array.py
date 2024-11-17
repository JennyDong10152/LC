class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left < right:
            mid = left + (right-left)//2
            midV = nums[mid]

            if midV <= nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]