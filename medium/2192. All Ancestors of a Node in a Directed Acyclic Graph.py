class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        ans = [set() for _ in range(n)]
        degree = [0] * n

        for prev, node in edges:
            graph[prev].append(node)
            degree[node] += 1
        
        q = deque()
        for i in range(n):
            if not degree[i]:
                q.append(i)

        while q:
            curr = q.popleft()
            for neighbor in graph[curr]:
                degree[neighbor] -= 1
                ans[neighbor].add(curr)
                ans[neighbor].update(ans[curr])
                if not degree[neighbor]:
                    q.append(neighbor)
        return [sorted(i) for i in ans]
        