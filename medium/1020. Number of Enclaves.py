class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        parent = {(i, j) : (i, j) for i in range(m) for j in range(n) if grid[i][j]}
        directions = [(-1, 0), (0, -1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    for di, dj in directions:
                        new_i = i + di
                        new_j = j + dj
                        if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j]:
                            self.union(parent, (i, j), (new_i, new_j))
        roots = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (not i or not j or i == m-1 or j == n-1):
                    roots.append(self.find(parent, (i, j)))
        
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    root = self.find(parent, (i, j))
                    if root not in roots:
                        cnt += 1
        return cnt
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]