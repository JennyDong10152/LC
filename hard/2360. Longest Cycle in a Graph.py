class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = set()
        degree = [0] * n

        for start, end in enumerate(edges):
            if end != -1:
                degree[end] += 1

        q = deque()
        for i in range(n):
            if not degree[i]:
                q.append(i)
        while q:
            curr = q.popleft()
            visited.add(curr)
            neighbor = edges[curr]
            if neighbor != -1:
                degree[neighbor] -= 1
                if not degree[neighbor]:
                    q.append(neighbor)

        max_cycle = -1
        for node in range(n):
            if node not in visited:
                temp_cycle = 0
                curr = node
                while curr not in visited:
                    visited.add(curr)
                    temp_cycle += 1
                    curr = edges[curr]
                    if curr == -1:
                        break
                if curr == node:
                    max_cycle = max(max_cycle, temp_cycle)
        return max_cycle