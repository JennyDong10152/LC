class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid2)
        n = len(grid2[0])
        parent = {(i, j) : (i, j) for i in range(m) for j in range(n) if grid2[i][j]}
        direction = [(0, -1), (-1, 0)]
        islands = defaultdict(list)
        cnt = 0

        for i in range(m):
            for j in range(n):
                if grid2[i][j]:
                    for di, dj in direction:
                        new_i = i + di
                        new_j = j + dj
                        if 0 <= new_i < m and 0 <= new_j < n and grid2[new_i][new_j]:
                            self.union(parent, (i, j), (new_i, new_j))

        for x in parent:
            root = self.find(parent, x)
            islands[root].append(x)

        for root, cells in islands.items():
            if all(grid1[i][j] for i, j in cells):
                cnt += 1
        return cnt
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_y] = root_x
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]