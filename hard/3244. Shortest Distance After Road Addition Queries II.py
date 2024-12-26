class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        self.graph = defaultdict(list)
        for i in range(n-1):
            self.graph[i].append(i+1)

        answer = []
        for start, end in queries:
            self.graph[start].append(end)
            answer.append(self.search(n))
        return answer

    def search(self, n):
        distances = [n+1] * n
        distances[0] = 0
        queue = deque([0])
        visited = set([0])

        while queue:
            current = queue.popleft()
            if current == n-1:
                return distances[n-1]
            for neighbor in self.graph[current]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
        return -1