class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        grid = [[0 for _ in range(n)] for _ in range(m)]
        ans = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        num_islands = 0

        for i, j in positions:
            if grid[i][j] == 1:
                ans.append(num_islands)
                continue
            grid[i][j] = 1
            parent[(i, j)] = (i, j)
            num_islands += 1

            for di, dj in directions:
                new_i = i + di
                new_j = j + dj
                if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j]:
                    connected = self.union(parent, (new_i, new_j), (i, j))
                    if connected:
                        num_islands -= 1
            ans.append(num_islands)
        return ans
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y
            return True
        return False
    
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]