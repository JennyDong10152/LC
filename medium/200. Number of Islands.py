class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        parent = {(i,j):(i,j) for i in range(m) for j in range(n) if grid[i][j]=="1"}
        direction = [(0, -1), (-1, 0)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    for di, dj in direction:
                        new_i = i + di
                        new_j = j + dj
                        if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j]=="1":
                            self.union(parent, (i, j), (new_i, new_j))
        disjoint = set()
        for x in parent:
            root = self.find(parent, x)
            disjoint.add(root)
        return len(disjoint)
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_y] = root_x
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]