class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        degree = [0] * n

        for edge1, edge2 in edges:
            graph[edge1].append(edge2)
            graph[edge2].append(edge1)
            degree[edge1] += 1
            degree[edge2] += 1
        
        leaves = deque()
        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)
        
        while n > 2:
            size = len(leaves)
            n -= size
            for _ in range(size):
                curr = leaves.popleft()
                for leaf in graph[curr]:
                    degree[leaf] -= 1
                    if degree[leaf] == 1:
                        leaves.append(leaf)
        return list(leaves)