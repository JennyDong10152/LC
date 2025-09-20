class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[-1][-1]

        while left <= right:
            mid = left + (right - left) // 2
            rank = self.count(matrix, mid)
            if rank >= k:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def count(self, matrix, target):
        n = len(matrix)
        count = 0

        for i in range(n):
            j = n - 1
            while j >= 0 and matrix[i][j] > target:
                j -= 1
            if j >= 0:
                count += (j+1)
            else:
                break
        return count