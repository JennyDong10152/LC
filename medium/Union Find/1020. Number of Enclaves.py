class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        parent = {(i, j) : (i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j]}
        size = {(i, j) : 1 for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j]}
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    for di, dj in directions:
                        new_i = i + di
                        new_j = j + dj
                        if 0<=new_i<len(grid) and 0<=new_j<len(grid[0]) and grid[new_i][new_j]:
                            self.union(parent, size, (i, j), (new_i, new_j))
        
        boundaries = set()
        roots = set()
        for i, j in parent:
            root = self.find(parent, (i, j))
            if i == 0 or i == len(grid)-1 or j == 0 or j == len(grid[0])-1: 
                boundaries.add(root)
            roots.add(root)

        cnt = 0
        for i, j in roots:
            if (i, j) not in boundaries:
                cnt += size[(i, j)]
        
        return cnt
    
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