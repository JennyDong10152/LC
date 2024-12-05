class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        parent = {(i, j):(i, j) for i in range(m) for j in range(n) if grid[i][j]!=0}
        size = {(i, j): grid[i][j] for i in range(m) for j in range(n) if grid[i][j]!=0}
        direction = [(0, -1), (-1, 0)]
        max_size = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    for di, dj in direction:
                        new_i = i + di
                        new_j = j + dj
                        if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j]!=0:
                            self.union(parent, size, (i, j), (new_i, new_j))
        
        for x in parent:
            max_size = max(max_size, size[x])
        return max_size
    
    def union(self, parent, size, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y
            size[root_y] += size[root_x]
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]
