class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] > target:
                return False
            if row[-1] < target:
                continue
            if self.search(row, target):
                return True
        return False
    
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            midV = nums[mid]
            if midV == target: 
                return True
            if midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return False