class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for start, end in redEdges:
            graph[start].append((end, "red"))
        
        for start, end in blueEdges:
            graph[start].append((end, "blue"))
        
        answer = [-1] * n
        queue = deque([(0, 0, None)])
        visited = set()

        while queue:
            node, distance, prevColor = queue.popleft()
            visited.add((node, prevColor))
            if answer[node] == -1:
                answer[node] = distance
            for neighbor, color in graph[node]:
                if (neighbor, color) not in visited and prevColor != color:
                    queue.append((neighbor, distance+1, color))
        return answer