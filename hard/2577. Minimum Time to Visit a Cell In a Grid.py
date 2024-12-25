class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
            
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        heap = [(grid[0][0], 0, 0)] #distance, row, col

        while heap:
            distance, row, col = heappop(heap)
            if (row, col) == (rows-1, cols-1):
                return distance
            if (row, col) in visited:
                continue
            visited.add((row, col))
            for di, dj in directions:
                new_i = row + di
                new_j = col + dj
                if 0 <= new_i < rows and 0 <= new_j < cols:
                    waitTime = 1 if not (grid[new_i][new_j]-distance)%2 else 0
                    nextDistance = max(grid[new_i][new_j]+waitTime, distance+1)
                    heappush(heap, (nextDistance, new_i, new_j))
        return -1