class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        self.graph = defaultdict(list)
        for node1, node2, weight in edges:
            self.graph[node1].append((weight, node2))
            self.graph[node2].append((weight, node1))

        minNeighbor = [n + 1, n]
        for city in range(n):
            neighbors = self.search(city, distanceThreshold)
            if neighbors <= minNeighbor[0]:
                minNeighbor = [neighbors, city]
        return minNeighbor[1]

    def search(self, city, distanceThreshold):
        heap = [(0, city)]
        visited = set()

        while heap:
            distance, current = heappop(heap)
            if current in visited:
                continue
            visited.add(current)
            for weight, neighbor in self.graph[current]:
                newDistance = weight + distance
                if newDistance <= distanceThreshold and neighbor not in visited:
                    heappush(heap, (newDistance, neighbor))
        return len(visited)