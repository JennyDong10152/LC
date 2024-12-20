class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        direction = [(0, -1), (-1, 0)]
        parent = {(i, j): (i, j) for i in range(m) for j in range(n) if grid[i][j]}

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    for di, dj in direction:
                        new_i = i + di
                        new_j = j + dj
                        if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j]:
                            self.union(parent, (i, j), (new_i, new_j))

        island = defaultdict(list)
        for x, y in parent:
            root_x, root_y = self.find(parent, (x,y))
            island[(root_x, root_y)].append((x-root_x, y-root_y))
        return len(set(tuple(isl) for isl in island.values()))
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_y] = root_x
    
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]