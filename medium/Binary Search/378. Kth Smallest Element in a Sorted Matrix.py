class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
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
        cnt = 0
        n = len(matrix)
        for row in matrix:
            if row[-1] < target:
                cnt += n
            elif row[0] > target:
                break
            else:
                idx = 0
                while idx < n and row[idx] <= target:
                    idx += 1
                cnt += idx 
        return cnt