class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        parent = {(i, j): (i, j) for i in range(m) for j in range(n) if not grid[i][j]}
        boundary_set = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    for di, dj in directions:
                        new_i = i + di
                        new_j = j + dj
                        if 0 <= new_i < m and 0 <= new_j < n and not grid[new_i][new_j]:
                            self.union(parent, (i, j), (new_i, new_j))
        
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    root = self.find(parent, (i, j))
                    if not i or i == m - 1 or not j or j == n - 1:
                        boundary_set.add(root)
        
        island_roots = set(self.find(parent, (i, j)) for i in range(m) for j in range(n) if not grid[i][j])
        closed_islands = island_roots - boundary_set
        
        return len(closed_islands)

    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x]) 
        return parent[x]
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_y] = root_x