class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        degree = [0] * n
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
            for node in graph[curr]:
                degree[node] -= 1
                if not degree[node]:
                    q.append(node)
        return False