class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for node1, node2, weight in edges:
            graph[node1].append((node2, weight))
            graph[node2].append((node1, weight))

        minDistance = [n+1, 0] #reacheables, node
        for i in range(n):
            reacheables = self.search(i, graph, distanceThreshold, n)
            if reacheables <= minDistance[0]:
                minDistance = [reacheables, i]
        return minDistance[1]

    def search(self, start, graph, distanceThreshold, n):
        reacheable = set()
        distances = [float("inf")] * n
        distances[start] = 0
        heap = [(0, start)]
        
        while heap:
            distance, node = heappop(heap)
            if distance > distances[node]:
                continue
            for neighbor, weight in graph[node]:
                new_distance = distance + weight
                if new_distance <= distanceThreshold and new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    reacheable.add(neighbor)
                    heappush(heap, (new_distance, neighbor))
        return len(reacheable)