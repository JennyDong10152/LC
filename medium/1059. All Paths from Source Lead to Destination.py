class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            if u == destination:
                return False
            graph[v].append(u)
            degree[u] += 1
        
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