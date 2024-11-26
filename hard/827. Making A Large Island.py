class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        
        parent = {(i, j): (i, j) for i in range(N) for j in range(N) if grid[i][j]}
        
        size = {(i, j): 1 for i in range(N) for j in range(N) if grid[i][j]}
    
        directions = [(1, 0), (0, 1)]

        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    for di, dj in directions:
                        new_i = i + di
                        new_j = j + dj
                        if 0 <= new_i < N and 0 <= new_j < N and grid[new_i][new_j]:
                            self.union(parent, size, (i, j), (new_i, new_j))

        max_area = 0
        has_zero = False
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 0:
                    has_zero = True
                    adjacent_islands = set()
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        new_i = i + di
                        new_j = j + dj
                        if 0 <= new_i < N and 0 <= new_j < N and grid[new_i][new_j]:
                            adjacent_islands.add(self.find(parent, (new_i, new_j)))
                    area = 1 + sum(size[island] for island in adjacent_islands)
                    max_area = max(max_area, area)

        return max_area if has_zero else N * N
    
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]
    
    def union(self, parent, size, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y
            size[root_y] += size[root_x]
