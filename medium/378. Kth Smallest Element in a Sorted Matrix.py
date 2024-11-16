class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix) - 1

        left = matrix[0][0]
        right = matrix[m][m]

        while left <= right:
            mid = left + (right-left)//2
            cnt, cur_max = self.count(left, matrix, k, mid)
            if cnt == k:
                return cur_max
            if cnt > k:
                right = mid - 1
            else:
                left = mid + 1
        return left
            
        
    def count(self, cur_max, matrix, k, target):
        cnt = 0
        for i in range(len(matrix)):
            j = len(matrix) - 1
            while j >= 0 and matrix[i][j] > target:
                j -= 1
            if j >= 0:
                cnt += (j + 1)
                cur_max = max(cur_max, matrix[i][j])
            else:
                break
        return cnt, cur_max