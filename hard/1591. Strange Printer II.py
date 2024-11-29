class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        colors = set()
        graph = defaultdict(set)
        degree = defaultdict(int)

        m = len(targetGrid)
        n = len(targetGrid[0])
        bounds = defaultdict(lambda: [n, -1, m, -1])
        for i in range(m):
            for j in range(n):
                color = targetGrid[i][j]
                colors.add(color)
                left, right, top, bot = bounds[color]
                bounds[color] = min(left, j), max(right, j), min(top, i), max(bot, i)
        
        for color in colors:
            left, right, top, bot = bounds[color]
            for i in range(top, bot+1):
                for j in range(left, right+1):
                    if targetGrid[i][j] != color:
                        if color not in graph[targetGrid[i][j]]:
                            graph[targetGrid[i][j]].add(color)
                            degree[color] += 1
        q = deque()
        for color in colors:
            if not degree[color]:
                q.append(color)
        
        order = []
        while q:
            curr = q.popleft()
            order.append(q)
            for neighbor in graph[curr]:
                degree[neighbor] -= 1
                if not degree[neighbor]:
                    q.append(neighbor)
        return len(order) == len(colors)