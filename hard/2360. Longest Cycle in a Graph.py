class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        degree = [0] * n

        for u, v in enumerate(edges):
            if v != -1:
                degree[v] += 1
        
        q = deque()
        visited = set()
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
            if node in visited:
                continue
            curr = node
            temp_cycle = 0
            while not curr in visited:
                visited.add(curr)
                temp_cycle += 1
                curr = edges[curr]
                if curr == -1:
                    break
            if curr == node:
                max_cycle = max(max_cycle, temp_cycle)
        return max_cycle