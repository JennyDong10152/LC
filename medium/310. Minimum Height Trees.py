class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        degrees = [0] * n
        graph = defaultdict(set)
        
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            degrees[u] += 1
            degrees[v] += 1

        leaves = deque()
        
        for i in range(n):
            if degrees[i] == 1:
                leaves.append(i)
        
        while n > 2:
            num_leaves = len(leaves)
            n -= num_leaves
            
            for i in range(num_leaves):
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        leaves.append(neighbor)
        return list(leaves)