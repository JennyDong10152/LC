class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:

        self.m = len(grid)
        self.n = len(grid[0])
        self.visited = set()

        for i in range(self.m):
            for j in range(self.n):
                if (i, j) not in self.visited:
                    char = grid[i][j]
                    if self.search(grid, char, i, j, -1, -1, 0):
                        return True
        return False
    
    def search(self, grid, char, i, j, prev_i, prev_j, path):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or char != grid[i][j]:
            return False

        if (i,j) in self.visited:
            return path >= 4
        
        self.visited.add((i,j))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for di, dj in directions:
            new_i = i + di
            new_j = j + dj
            if new_i == prev_i and new_j == prev_j:
                continue
            if self.search(grid, char, new_i, new_j, i, j, path+1):
                return True
        return False