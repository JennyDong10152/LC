class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for city1, city2 in connections:
            graph[city1].append((city2, True))
            graph[city2].append((city1, False))
        
        queue = deque([0])
        count = 0
        visited = set()
        
        while queue:
            city = queue.popleft()
            visited.add(city)
            for neighbor, outgoing in graph[city]:
                if not neighbor in visited:
                    queue.append(neighbor)
                    if outgoing:
                        count += 1
        return count