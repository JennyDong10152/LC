class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        for node1, node2 in edges:
            if vals[node2] > 0:
                graph[node1].append(node2)
            if vals[node1] > 0:
                graph[node2].append(node1)
        
        stars = []
        for node, val in enumerate(vals):
            values = [vals[neighbor] for neighbor in graph[node]]
            values.sort(reverse = True)
            stars.append(val + sum(values[:k]))
        return max(stars)