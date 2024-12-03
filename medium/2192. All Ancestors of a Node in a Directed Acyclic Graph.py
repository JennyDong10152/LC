class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        degree = [0] * n
        ans = [set() for i in range(n)]

        for prev, node in edges:
            graph[prev].append(node)
            degree[node] += 1
        
        q = deque()
        for i in range(n):
            if not degree[i]:
                q.append(i)
        
        while q:
            curr = q.popleft()
            for node in graph[curr]:
                degree[node] -= 1
                ans[node].add(curr)
                ans[node].update(ans[curr])
                if not degree[node]:
                    q.append(node)
        return [sorted(list(i)) for i in ans]