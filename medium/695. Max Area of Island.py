class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        self.m = len(grid)
        self.n = len(grid[0])
        self.visited = set()

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    area = self.find(grid, i, j)
                    max_area = max(max_area, area)
        return max_area
    
    def find(self, grid, i, j):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or grid[i][j] == 0 or (i, j) in self.visited:
            return 0
        
        self.visited.add((i, j))
        grid[i][j] = 0
        return 1 + self.find(grid, i+1, j) + self.find(grid, i-1, j) + self.find(grid, i, j-1) + self.find(grid, i, j+1)