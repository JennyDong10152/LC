class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m = len(grid)
        n = len(grid[0])
        parent = {(i, j) : (i, j) for i in range(m) for j in range(n) if grid[i][j]}
        size = {(i, j) : 1 for i in range(m) for j in range(n) if grid[i][j]}
        direction = [(0, -1), (-1, 0)]

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    for di, dj in direction:
                        new_i = i + di
                        new_j = j + dj
                        if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j]:
                            self.union(parent, size, (i, j), (new_i, new_j))
        
        for x in parent:
            if x == parent[x]:
                max_area = max(max_area, size[x])
        return max_area

    def union(self, parent, size, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_y] = root_x
            size[root_x] += size[root_y]
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]