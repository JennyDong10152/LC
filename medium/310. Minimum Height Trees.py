class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        degree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        q = deque()
        for i in range(n):
            if degree[i] == 1:
                q.append(i)

        while n > 2:
            num_leaves = len(q)
            n -= num_leaves
            for _ in range(num_leaves):
                curr = q.popleft()
                for leaf in graph[curr]:
                    degree[leaf] -= 1
                    if degree[leaf] == 1:
                        q.append(leaf)
        return list(q)