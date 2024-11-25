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
            cur = q.popleft()
            if cur == source:
                return True

            for prev in graph[cur]:
                degree[prev] -= 1
                if not degree[prev]:
                    q.append(prev)
        return False