class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] > target:
                return False
            elif row[-1] < target:
                continue
            elif self.search(row, target):
                return True
        return False
    
    def search(self, row, target):
        left = 0
        right = len(row) - 1
        while left <= right:
            mid = left + (right - left) // 2
            midV = row[mid]
            if midV == target:
                return True
            elif midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return False