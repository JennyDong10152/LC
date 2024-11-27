class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        
        cnt = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1':
                    self.search(grid, i, j)
                    cnt += 1
        return cnt
    
    def search(self, grid, i, j):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or grid[i][j] == '0':
            return 
        grid[i][j] = "0"
        self.search(grid, i+1, j)
        self.search(grid, i-1, j)
        self.search(grid, i, j+1)
        self.search(grid, i, j-1)