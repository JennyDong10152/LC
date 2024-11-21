class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        for i in mat[0]:
            target = i
            for j in range(1, len(mat)):
                if not self.search(target, mat[j]):
                    break
                if j == len(mat) - 1:
                    return target
        return -1
    
    def search(self, target, nums):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            midV = nums[mid]
            if midV == target:
                return True
            elif midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return False