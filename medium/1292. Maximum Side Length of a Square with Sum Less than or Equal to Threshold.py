class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        if min(min(i) for i in mat) > threshold:
            return 0
        
        left = 1
        right = min(m, n)
        prefix = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                prefix[i+1][j+1] = mat[i][j] + prefix[i+1][j] + prefix[i][j+1] - prefix[i][j]

        while left <= right:
            mid = left + (right-left)//2
            if self.isValid(prefix, mid, threshold):
                left = mid + 1
            else:
                right = mid - 1
        return right
    
    def isValid(self, prefix, idx, threshold):
        for i in range(idx, len(prefix)):
            for j in range(idx, len(prefix[0])):
                curr = prefix[i][j] - prefix[i-idx][j] - prefix[i][j-idx] + prefix[i-idx][j-idx]
                if curr <= threshold:
                    return True
        return False