class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        self.graph = defaultdict(list)
        for i in range(n-1):
            self.graph[i].append(i+1)
        answer = []
        for start, end in queries:
            self.graph[start].append(end)
            answer.append(self.search(n-1))
        return answer

    def search(self, n):
        heap = [(0, 0)]
        visited = set([0])

        while heap:
            distance, current = heappop(heap)
            if current == n:
                return distance
            for neighbor in self.graph[current]:
                if not neighbor in visited:
                    visited.add(neighbor)
                    heappush(heap, (distance+1, neighbor))
        return -1