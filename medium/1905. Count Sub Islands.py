class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])

        parent = {(i, j) : (i, j) for i in range(m) for j in range(n) if grid2[i][j]}
        directions = [(-1, 0), (0, -1)]
        for i in range(m):
            for j in range(n):
                if grid2[i][j]:
                    for di, dj in directions:
                        new_i = i + di
                        new_j = j + dj
                        if 0 <= new_i < m and 0 <= new_j < n and grid2[new_i][new_j] == 1:
                            self.union(parent, (i, j), (new_i, new_j))
        islands = {}
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    root = self.find(parent, (i, j))
                    if root not in islands:
                        islands[root] = []
                    islands[root].append((i, j))
        cnt = 0
        for root, cells in islands.items():
            is_sub_island = all(grid1[i][j] == 1 for i, j in cells)
            if is_sub_island:
                cnt += 1
        return cnt
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y
    
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]