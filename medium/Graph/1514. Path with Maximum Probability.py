class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for [node1, node2], prob in zip(edges, succProb):
            graph[node1].append((prob, node2))
            graph[node2].append((prob, node1))
        
        maxProb = [0.0] * n
        maxProb[start_node] = 1.0
        heap = [(-1.0, start_node)]

        while heap:
            prob, node = heappop(heap)
            prob = -prob

            if node == end_node:
                return prob
            
            for nextProb, neighbor in graph[node]:
                newProb = nextProb * prob
                if newProb > maxProb[neighbor]:
                    maxProb[neighbor] = newProb
                    heappush(heap, (-newProb, neighbor))
        return 0.0