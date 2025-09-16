class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n-1][n-1]

        while left <= right:
            mid = left + (right - left) // 2
            count = self.check(matrix, mid)
            if count >= k:
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def check(self, matrix, mid):
        n = len(matrix)
        count = 0

        for i in range(n):
            j = n-1
            while j >= 0 and matrix[i][j] > mid:
                j -= 1
            if j >= 0:
                count += (j+1)
            else:
                break
        return count