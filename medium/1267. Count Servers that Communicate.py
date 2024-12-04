class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        parent = {(i, j) : (i, j) for i in range(m) for j in range(n) if grid[i][j]}
        size = {(i, j) : 1 for i in range(m) for j in range(n) if grid[i][j]}

        for i in range(m):
            row_servers = [j for j in range(n) if grid[i][j] == 1]
            for k in range(1, len(row_servers)):
                self.union(parent, size, (i, row_servers[0]), (i, row_servers[k]))

        for j in range(n):
            col_servers = [i for i in range(m) if grid[i][j] == 1]
            for k in range(1, len(col_servers)):
                self.union(parent, size, (col_servers[0], j) , (col_servers[k], j))

        group_count = defaultdict(int)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    root = self.find(parent, (i, j))
                    group_count[root] += 1

        return sum(count for count in group_count.values() if count > 1)

    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]

    def union(self, parent, size, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            if size[root_x] < size[root_y]:
                root_x, root_y = root_y, root_x
            parent[root_y] = root_x
            size[root_x] += size[root_y]