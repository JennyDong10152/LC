class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        total = 4 * n * n #top, right, bot, left
        parent = [i for i in range(total)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                idx = 4 * (i * n + j)
                cell = grid[i][j]
                if cell == " ":
                    self.union(parent, idx, idx + 1)
                    self.union(parent, idx, idx + 2)
                    self.union(parent, idx, idx + 3)
                if cell == "/":
                    self.union(parent, idx, idx + 3)
                    self.union(parent, idx + 1, idx + 2)
                if cell == "\\":
                    self.union(parent, idx, idx + 1)
                    self.union(parent, idx + 2, idx + 3)
                if i < n-1:
                    self.union(parent, idx+2, idx+(4*n))
                if j < n-1:
                    self.union(parent, idx+1, idx+4+3)
        ans = 0
        for i in range(total):
            if i == self.find(parent, i):
                ans += 1
        return ans

    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y
            return 1
        return 0

    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]