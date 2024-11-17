class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        for row in range(len(grid)):
            idx = self.search(grid[row])
            cnt += (len(grid[row])-idx)
        return cnt
    
    def search(self, row):
        left = 0
        right = len(row)

        while left < right:
            mid = left + (right-left)//2
            midV = row[mid]
            if midV >= 0:
                left = mid + 1
            else:
                right = mid
        return left
