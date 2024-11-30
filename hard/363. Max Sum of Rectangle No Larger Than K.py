class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        max_area = -float("inf")

        for left in range(n):
            prefix = [0]*m
            for right in range(left, n):
                for r in range(m):
                    prefix[r] += matrix[r][right]
                
                sorted_sums = [0]
                curr = 0
                for val in prefix:
                    curr += val
                    #curr - k <= target
                    idx = self.search(sorted_sums, curr-k)
                    if 0 <= idx < len(sorted_sums):
                        max_area = max(max_area, curr-sorted_sums[idx])
                    idx_insert = self.search(sorted_sums, curr)
                    sorted_sums.insert(idx_insert, curr)
        return max_area
    
    def search(self, nums, target):
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left + (right-left)//2
            midV = nums[mid]
            if midV >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left