class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        for row in matrix:
            if target > row[-1]:
                continue
            if target < row[0]:
                return False
            else:
                if self.search(row, target):
                    return True
        return False
    
    
    def search(self, row, target):
        left = 0
        right = len(row)-1

        while left <= right:
            mid = left + (right- left)//2
            midV = row[mid]
            if midV == target:
                return True
            if midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
