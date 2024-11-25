class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for _ in range(n)]
        graph = defaultdict(set)
        degree = [0] * n

        for parent, child in edges:
            graph[parent].add(child)
            degree[child] += 1
        
        q = deque()
        for i in range(n):
            if not degree[i]:
                q.append(i)

        while q:
            curr = q.popleft()
            for child in graph[curr]:
                ans[child].update(ans[curr])
                ans[child].add(curr)
                degree[child] -= 1
                if not degree[child]:
                    q.append(child)
        return [sorted(list(i)) for i in ans]