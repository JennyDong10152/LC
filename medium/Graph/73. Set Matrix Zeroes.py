class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        firstRow = False
        firstCol = False
        
        for row in range(m):
            for col in range(n):
                if not matrix[row][col]:
                    if not row:
                        firstRow = True
                    if not col:
                        firstCol = True
                    
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, m):
            for col in range(1, n):
                if not matrix[row][0] or not matrix[0][col]:
                    matrix[row][col] = 0
        
        if firstRow:
            for col in range(n):
                matrix[0][col] = 0
        if firstCol:
            for row in range(m):
                matrix[row][0] = 0