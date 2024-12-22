class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left + (right-left)//2
            midV = nums[mid]
            if midV == target:
                return True
                
            if nums[left] == midV == nums[right]:
                left += 1
                right -= 1 
                continue
            elif nums[left] <= midV:
                if nums[left] <= target < midV:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if midV < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False