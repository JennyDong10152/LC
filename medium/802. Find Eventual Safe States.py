class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        degree = [0] * n
        reverse_graph = defaultdict(list)

        for start, ends in enumerate(graph):
            for end in ends:
                reverse_graph[end].append(start)
                degree[start] += 1
        
        q = deque()
        for i in range(n):
            if not degree[i]:
                q.append(i)
        ans = []
        while q:
            curr = q.popleft()
            ans.append(curr)
            for neighbor in reverse_graph[curr]:
                degree[neighbor] -= 1
                if not degree[neighbor]:
                    q.append(neighbor)
        return sorted(ans)
    #reviewed