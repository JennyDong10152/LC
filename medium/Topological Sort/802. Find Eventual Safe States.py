class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        reverse_graph = defaultdict(list)
        degree = [0] * (len(graph))

        for start, ends in enumerate(graph):
            for end in ends:
                reverse_graph[end].append(start)
                degree[start] += 1
        order = deque()
        ans = []
        for i in range(len(graph)):
            if not degree[i]:
                order.append(i)
        while order:
            curr = order.popleft()
            ans.append(curr)
            for node in reverse_graph[curr]:
                degree[node] -= 1
                if not degree[node]:
                    order.append(node)
        return sorted(ans)