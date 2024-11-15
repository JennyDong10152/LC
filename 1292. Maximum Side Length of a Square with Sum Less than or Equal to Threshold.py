class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        if min(min(line) for line in mat) > threshold:
            return 0
        
        m = len(mat)
        n = len(mat[0])

        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = mat[i][j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j]
                #stores side lengths
        
        left = 1
        right = min(m, n)
        ans = 0

        while left <= right:
            mid = left + (right-left)//2
            if self.count(mid, prefix, threshold):
                ans = mid 
                left = mid + 1
            else:
                right = mid - 1
        return ans

    def count(self, idx, prefix, threshold):
        for i in range(idx, len(prefix)):
            for j in range(idx, len(prefix[0])):
                current = prefix[i][j] - prefix[i-idx][j] - prefix[i][j-idx] + prefix[i-idx][j-idx]
                if current <= threshold:
                    return True
        return False