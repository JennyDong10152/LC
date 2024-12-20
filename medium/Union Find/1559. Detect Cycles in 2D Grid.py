class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        parent = {(i, j) : (i, j) for i in range(m) for j in range(n)}

        for i in range(m):
            for j in range(n):
                if i>0 and grid[i][j] == grid[i-1][j]:
                    if self.find(parent, (i, j)) == self.find(parent, (i-1, j)):
                        return True
                    self.union(parent, (i-1, j), (i, j))
                if j>0 and grid[i][j-1] == grid[i][j]:
                    if self.find(parent, (i, j-1)) == self.find(parent, (i, j)):
                        return True
                    self.union(parent, (i, j-1), (i, j))
        return False
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y
    
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]
        