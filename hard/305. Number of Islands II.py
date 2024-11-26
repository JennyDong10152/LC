class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        grid = [[0 for _ in range(n)] for _ in range(m)]

        ans = []

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        num_island = 0
        for i, j in positions:
            if grid[i][j] == 1:
                ans.append(num_island)
                continue
            adjacent_islands = set()
            grid[i][j] = 1
            parent[(i, j)] = (i, j)
            num_island += 1

            for di, dj in directions:
                new_i = i + di
                new_j = j + dj
                if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j]:
                    if self.union(parent, (i, j), (new_i, new_j)):
                        num_island -= 1
            ans.append(num_island)
        return ans
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x == root_y:
            return False
        parent[root_x] = root_y
        return True
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]