class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for _ in range(n)]
        degrees = [0] * n
        relation = defaultdict(list)

        for parent, child in edges:
            degrees[child] += 1
            relation[parent].append(child)
        
        q = deque()
        for i in range(n):
            if not degrees[i]:
                q.append(i)
        
        while q:
            cur = q.popleft()
            for child in relation[cur]:
                ans[child].update(ans[cur])
                ans[child].add(cur)
                degrees[child] -= 1
                if not degrees[child]:
                    q.append(child)
        return [sorted(list(ancestors)) for ancestors in ans]