class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for [node1, node2], probability in zip(edges, succProb):
            graph[node1].append((probability, node2))
            graph[node2].append((probability, node1))

        maxProb = [0.0] * n
        maxProb[start_node] = 1.0
        heap = [(-1.0, start_node)]

        while heap:
            currentProb, current = heappop(heap)
            currentProb = -currentProb

            if current == end_node:
                return currentProb

            for nextProb, neighbor in graph[current]:
                newProb = nextProb * currentProb
                if newProb > maxProb[neighbor]:
                    maxProb[neighbor] = newProb
                    heappush(heap, (-newProb, neighbor))
        return 0.0