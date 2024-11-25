class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        max_sum = -float('inf')

        for left in range(n):
            prefix = [0] * m
            for right in range(left, n):
                for r in range(m):
                    prefix[r] += matrix[r][right]
                
                cur_sum = 0
                sorted_sums = [0]

                for val in prefix:
                    cur_sum += val
                    #curr - k <= target
                    idx = self.search(sorted_sums, cur_sum-k)
                    if 0 <= idx < len(sorted_sums):
                        max_sum = max(max_sum, cur_sum-sorted_sums[idx])
                    idx_inserted = self.search(sorted_sums, cur_sum)
                    sorted_sums.insert(idx_inserted, cur_sum)
        return max_sum

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
