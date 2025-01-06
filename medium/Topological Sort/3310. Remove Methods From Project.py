class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = [0] * n
        for start, end in invocations:
            graph[start].append(end)
            degree[end] += 1
        
        visited = set()
        queue = deque([k])
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            for neighbor in graph[node]:
                degree[neighbor] -= 1
                queue.append(neighbor)

        if all([not degree[node] for node in visited]):
            return list(set(range(n)) - visited)
        return list(range(n))