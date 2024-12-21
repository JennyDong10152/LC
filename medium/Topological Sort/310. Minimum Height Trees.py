class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        degree = [0] * n
        graph = defaultdict(list)
        for node1, node2 in edges:
            degree[node1] += 1
            degree[node2] += 1
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        queue = deque()
        
        for node in range(n):
            if degree[node] == 1:
                queue.append(node)

        while n > 2:
            size = len(queue)
            n -= size
            for _ in range(size):
                leaf = queue.popleft()
                for parent in graph[leaf]:
                    degree[parent] -= 1
                    if degree[parent] == 1:
                        queue.append(parent)
        return list(queue)