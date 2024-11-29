class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        parent = {(i, j) : (i, j) for i in range(m) for j in range(n) if grid[i][j] == "1"}
        directions = [(-1, 0), (0, -1)]
        disjoint = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    for di, dj in directions:
                        new_i = i + di
                        new_j = j + dj
                        if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == "1":
                            self.union(parent, (i, j), (new_i, new_j))

        for x in parent:
            disjoint.add(self.find(parent, x))
        return len(disjoint)
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y
        
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]