class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        degree = [0] * n

        for prev, node in enumerate(edges):
            if node != -1:
                degree[node] += 1
        
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
        for i in range(n):
            if i in visited:
                continue
            temp_cycle = 0
            curr = i
            while not curr in visited:
                visited.add(curr)
                curr = edges[curr]
                temp_cycle += 1
                if curr == -1:
                    break
            if i == curr:
                max_cycle = max(max_cycle, temp_cycle)
        return max_cycle
