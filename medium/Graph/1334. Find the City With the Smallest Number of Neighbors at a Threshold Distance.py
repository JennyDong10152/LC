class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        self.graph = defaultdict(list)
        for node1, node2, weight in edges:
            self.graph[node1].append((node2, weight))
            self.graph[node2].append((node1, weight))

        minNeighbor = [n + 1, n]  # numNeighbors, node
        for city in range(n):
            neighbors = self.search(city, distanceThreshold)
            if neighbors <= minNeighbor[0]:
                minNeighbor = [neighbors, city]
        return minNeighbor[1]

    def search(self, city: int, distanceThreshold: int) -> int:
        heap = [(0, city)] 
        visited = set()

        while heap:
            distance, current = heappop(heap)
            if current in visited:
                continue
            visited.add(current)

            for neighbor, weight in self.graph[current]:
                new_distance = distance + weight
                if new_distance <= distanceThreshold and neighbor not in visited:
                    heappush(heap, (new_distance, neighbor))        
        return len(visited) - 1