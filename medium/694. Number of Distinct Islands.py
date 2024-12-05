class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        parent = {(i, j): (i, j) for i in range(m) for j in range(n) if grid[i][j]}
        direction = [(0, -1), (-1, 0)]

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    for di, dj in direction:
                        new_i = i + di
                        new_j = j + dj
                        if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j]:
                            self.union(parent, (i, j), (new_i, new_j))

        islands = defaultdict(list)
        for i, j in parent:
            root_i, root_j = self.find(parent, (i, j))
            islands[(root_i, root_j)].append((root_i-i, root_j-j))
        return len(set(tuple(isl) for isl in islands.values()))

    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y
    
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]