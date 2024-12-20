class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        parent = {(i, j) : (i, j) for i in range(m) for j in range(n) if grid[i][j]}
        size = {(i, j) : 1 for i in range(m) for j in range(n) if grid[i][j]}
        directions = [(-1, 0), (0, -1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    for di, dj in directions:
                        new_i = i + di
                        new_j = j + dj
                        if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j]:
                            self.union(parent, size, (i, j), (new_i, new_j))
        boundaries = set()
        roots = set()
        for i, j in parent:
            if not i or not j or i == m-1 or j == n-1:
                boundaries.add(self.find(parent, (i, j)))
            roots.add(self.find(parent, (i, j)))
        
        cnt = 0
        for x in parent:
            if x not in boundaries and x == parent[x]:
                cnt += size[x]
        return cnt
    
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