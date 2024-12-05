class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        parent = {(i, j):(i, j) for i in range(n) for j in range(n) if grid[i][j]}
        size = {(i, j) : 1 for i in range(n) for j in range(n) if grid[i][j]}
        two_direction = [(-1, 0), (0, -1)]
        four_direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        maxArea = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    for di, dj in two_direction:
                        new_i = i + di
                        new_j = j + dj
                        if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j]:
                            self.union(parent, size, (i, j), (new_i, new_j))
        hasZero = False
        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    hasZero = True
                    islands = set()
                    for di, dj in four_direction:
                        new_i = i + di
                        new_j = j + dj
                        if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j]:
                            islands.add(self.find(parent, (new_i, new_j)))
                    temp = 1 + (sum(size[root] for root in islands))
                    maxArea = max(maxArea, temp)
        return maxArea if hasZero else n*n
    
    def union(self, parent, size, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_y] = root_x
            size[root_x] += size[root_y]
    
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]