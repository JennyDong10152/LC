class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        left = matrix[0][0]
        right = matrix[m-1][m-1]

        while left <= right:
            mid = left + (right-left)//2
            cnt = self.search(matrix, mid)
            if cnt >= k:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def search(self, mat, target):
        cnt = 0
        for i in range(len(mat)):
            j = len(mat[0])-1
            while j >= 0 and mat[i][j] > target:
                j -= 1
            if j >= 0:
                cnt += (j+1)
            else:
                break
        return cnt
