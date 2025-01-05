class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for start, end in connections:
            graph[start].append((end, True))
            graph[end].append((start, False))

        count = 0
        queue = deque([0])
        visited = set()

        while queue:
            current = queue.popleft()
            visited.add(current)
            for neighbor, outgoing in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    if outgoing:
                        count += 1
        return count