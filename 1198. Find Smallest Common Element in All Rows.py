class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        idx = 0
        for i in range(len(mat[0])):
            target = mat[0][i]
            
            for row in range(1,len(mat)):
                found = self.search(mat[row], target)
                if not found:
                    break
                if row == len(mat)-1:
                    return target
        return -1
    
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = left + (right-left)//2
            midV = nums[mid]

            if midV == target:
                return True
            if midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return False