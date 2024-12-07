class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        total = 4 * n * n
        parent = [i for i in range(total)]

        for i in range(n):
            for j in range(n):
                cell = grid[i][j]
                idx = 4 * (i*n + j) #top(0), right(1), bot(2), left(3)
                if cell == " ":
                    self.union(parent, idx, idx+1)
                    self.union(parent, idx, idx+2)
                    self.union(parent, idx, idx+3)
                elif cell == "/":
                    self.union(parent, idx, idx+3)
                    self.union(parent, idx+1, idx+2)
                elif cell == "\\":
                    self.union(parent, idx, idx+1)
                    self.union(parent, idx+2, idx+3)
                if i < n-1:
                    self.union(parent, idx+2, (idx+4*n))
                if j < n-1:
                    self.union(parent, idx+1, (idx+4+3))
        regions = 0
        for i in range(total):
            root_i = self.find(parent, i)
            if root_i == i:
                regions += 1
        return regions
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_y] = root_x
    
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]