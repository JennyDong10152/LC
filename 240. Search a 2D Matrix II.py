class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        for i in range(len(matrix)):
            if matrix[i][-1] < target:
                continue
            elif matrix[i][0] > target:
                return False
            else:
                if self.search(matrix[i], target):
                    return True
        return False
    
    def search(self, interval, target):
        left = 0
        right = len(interval)-1
        while left <= right:
            mid = left + (right-left)//2
            midV = interval[mid]

            if midV == target:
                return True
            if midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return False