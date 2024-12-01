class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        parent = {}
        bounds = defaultdict(lambda: [m, -1, n, -1])
        m = len(targetGrid)
        n = len(targetGrid[0])
        graph = defaultdict(list)
        colors = set()
        degree = defaultdict(int)

        for i in range(m):
            for j in range(n):
                color = targetGrid[i][j]
                colors.add(color)
                top, bot, left, right = bounds[color]
                bounds[color] = [min(top, i), max(bot, i), min(left, j), max(right, j)]
        
        for color in colors:
            top, bot, left, right = bounds[color]
            for i in range(top, bot+1):
                for j in range(left, right+1):
                    if color != targetGrid[i][j]:
                        if not color in graph[targetGrid[i][j]]:
                            graph[targetGrid[i][j]].append(color)
                            degree[color] += 1
        
        q = deque()
        for color in colors:
            if not degree[color]:
                q.append(color)

        order = []
        while q:
            curr = q.popleft()
            order.append(curr)
            for neighbor in graph[curr]:
                degree[neighbor] -= 1
                if not degree[neighbor]:
                    q.append(neighbor)
        return len(order) == len(colors)