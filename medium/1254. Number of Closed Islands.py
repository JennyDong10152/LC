class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        parent = {(i, j) : (i, j) for i in range(m) for j in range(n) if not grid[i][j]}
        direction = [(0, -1), (-1, 0)]

        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    for di, dj in direction:
                        new_i = i + di
                        new_j = j + dj
                        if 0 <= new_i < m and 0 <= new_j < n and not grid[new_i][new_j]:
                            self.union(parent, (i, j), (new_i, new_j))
        
        boundary_roots = set()
        roots = set()
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    root = self.find(parent, (i, j))
                    roots.add(root)
                    if not i or not j or i == m-1 or j == n-1:
                        boundary_roots.add(root)
        return len(roots) - len(boundary_roots)
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y
    
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]