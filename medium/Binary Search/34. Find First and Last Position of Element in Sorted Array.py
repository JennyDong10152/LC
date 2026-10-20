class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first = self.search(nums, target, True)
        second = self.search(nums, target, False)
        return [first, second]
    
    def search(self, nums, target, isFirst):
        left = 0
        right = len(nums) - 1
        ans = -1

        while left <= right:
            mid = left + (right-left)//2
            midV = nums[mid]
            if nums[mid] == target:
                ans = mid
                if isFirst:
                    right = mid-1
                else:
                    left = mid + 1

            elif midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return ans