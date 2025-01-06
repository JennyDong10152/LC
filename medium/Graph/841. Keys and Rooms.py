class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        total = len(rooms)
        visited = set()
        queue = deque([0])

        while queue:
            current = queue.popleft()
            visited.add(current)
            for neighbor in rooms[current]:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
        return total == len(visited)