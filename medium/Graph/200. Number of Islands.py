class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        count = 0

        for row in range(self.m):
            for col in range(self.n):
                if self.grid[row][col] == '1':
                    self.search(row, col)
                    count += 1
        return count
    
    def search(self, row, col):
        if row < 0 or row >= self.m or col < 0 or col >= self.n or self.grid[row][col] == '0':
            return 
        self.grid[row][col] = '0'
        self.search(row-1, col)
        self.search(row+1, col)
        self.search(row, col-1)
        self.search(row, col+1)