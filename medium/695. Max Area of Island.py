class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        self.m = len(grid)
        self.n = len(grid[0])

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.search(grid, i, j))
        return max_area
    
    def search(self, grid, i, j):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or not grid[i][j]:
            return 0
        
        grid[i][j] = 0
        return 1 + self.search(grid, i-1, j) + self.search(grid, i+1, j) + self.search(grid, i ,j-1) + self.search(grid, i, j+1)