class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        self.graph = [[] for _ in range(n)]
        for i in range(n-1):
            self.graph[i].append(i+1)
        answer = []
        for start, end in queries:
            self.graph[start].append(end)
            answer.append(self.search(n))
        return answer

    def search(self, n):
        queue = deque([0])
        distances = [n+1] * n
        distances[0] = 0
        visited = set([0])

        while queue:
            node = queue.popleft()
            if node == n-1:
                return distances[node]
            for neighbor in self.graph[node]:
                if neighbor in visited:
                    continue
                distances[neighbor] = distances[node]+1
                queue.append(neighbor)
                visited.add(neighbor)
        return -1