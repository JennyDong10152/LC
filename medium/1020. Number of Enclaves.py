class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        parent = {(i, j): (i, j) for i in range(m) for j in range(n) if grid[i][j]}
        border_roots = set()
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                            self.union(parent, (i, j), (ni, nj))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                    border_roots.add(self.find(parent, (i, j)))

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    root = self.find(parent, (i, j))
                    if root not in border_roots:
                        cnt += 1

        return cnt

    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y

    def find(self, parent, x):
        if x not in parent:
            return x
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]
