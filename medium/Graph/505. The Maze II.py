class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if not maze or not maze[0]:
            return -1
            
        m = len(maze)
        n = len(maze[0])
        visited = set()
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        heap = [(0, start[0], start[1])] #steps, x, y

        while heap:
            distance, x, y = heappop(heap)

            if x == destination[0] and y == destination[1]:
                return distance
            if (x,y) in visited:
                continue

            visited.add((x,y))
            for dx, dy in directions:
                steps = 0
                new_x = x
                new_y = y
                while (0 <= new_x + dx < m and 0 <= new_y + dy < n and maze[new_x + dx][new_y + dy] != 1):
                    steps += 1
                    new_x += dx
                    new_y += dy

                if (new_x, new_y) in visited:
                    continue
                heappush(heap, (steps + distance, new_x, new_y))
        return -1