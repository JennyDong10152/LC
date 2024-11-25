class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        degree = [0] * n
        graph = defaultdict(list)

        for start, end in edges:
            if start == destination:
                return False
            graph[end].append(start)
            degree[start] += 1
        
        q = deque([destination])
        while q:
            curr = q.popleft()
            if curr == source:
                return True
            for neighbor in graph[curr]:
                degree[neighbor] -= 1
                if not degree[neighbor]:
                    q.append(neighbor)
        return False
        
