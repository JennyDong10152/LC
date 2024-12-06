class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
            
        graph = defaultdict(list)
        degree = [0] * n

        for edge1, edge2  in edges:
            graph[edge1].append(edge2)
            graph[edge2].append(edge1)
            degree[edge1] += 1
            degree[edge2] += 1

        leaves = deque()
        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            for _ in range(len(leaves)):
                curr = leaves.popleft()
                for node in graph[curr]:
                    degree[node] -= 1
                    if degree[node] == 1:
                        leaves.append(node)
        return list(leaves)
