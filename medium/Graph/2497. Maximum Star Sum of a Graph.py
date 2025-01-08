class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        maxSum = -float("inf")

        for node1, node2 in edges:
            if vals[node1] > 0:
                graph[node2].append(node1)
            if vals[node2] > 0:
                graph[node1].append(node2)
        
        for num in range(len(vals)):
            val = [vals[node] for node in graph[num]]
            val.sort(reverse = True)
            maxSum = max(maxSum, vals[num] + sum(val[:k]))
        return maxSum