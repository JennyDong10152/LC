class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        self.k = k
        row_order = self.sort(rowConditions)
        col_order = self.sort(colConditions)

        if not row_order or not col_order:
            return []

        col_order = {x : i for i, x in enumerate(col_order)}
        grid = [[0 for _ in range(k)] for _ in range(k)]
        
        for i, x in enumerate(row_order):
            if not x in col_order:
                break
            j = col_order[x]
            grid[i][j] = x
        
        for row in grid:
            if not any(row):
                return []
        return grid
    
    def sort(self, relations):
        graph = defaultdict(list)
        degree = [0] * (self.k+1)

        for prev, x in relations:
            if not x in graph[prev]:
                graph[prev].append(x)
                degree[x] += 1
        
        q = deque()
        for i in range(1, self.k+1):
            if not degree[i]:
                q.append(i)

        order = []
        while q:
            curr = q.popleft()
            order.append(curr)
            for neighbor in graph[curr]:
                degree[neighbor] -= 1
                if not degree[neighbor]:
                    q.append(neighbor)
        return order if not any(degree) else []