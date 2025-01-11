class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        queue = deque([0])
        visited = set()
        
        while queue:
            room = queue.popleft()
            if room in visited:
                continue
            visited.add(room)
            for nextRoom in rooms[room]:
                queue.append(nextRoom)
        return len(visited) == n