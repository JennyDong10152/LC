class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        parent = {(i, j) : (i, j) for i in range(m) for j in range(n) if grid[i][j]}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    for di, dj in directions:
                        new_i = i + di
                        new_j = j + dj
                        if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j]:
                            self.union(parent, (i, j), (new_i, new_j))

        islands = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    root = self.find(parent, (i, j))
                    if root not in islands:
                        islands[root] = []
                    islands[root].append((i, j))

        shapes = set()
        for shape in islands.values():
            base_x, base_y = min(shape)
            relative_shape = [(x - base_x, y - base_y) for x, y in shape]
            normalized = self.normalize(relative_shape)
            shapes.add(normalized)
        return len(shapes)

    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]

    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_y] = root_x

    def normalize(self, shape):
        transforms = []
        for rotate in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            for reflect in [(1, 1), (1, -1)]:
                transformed = [(rotate[0] * x, rotate[1] * y) for x, y in shape]
                transformed = [(reflect[0] * x, reflect[1] * y) for x, y in transformed]
                transformed = sorted(transformed)
                base_x, base_y = transformed[0]
                normalized = [(x - base_x, y - base_y) for x, y in transformed]
                transforms.append(tuple(normalized))
        return min(transforms)