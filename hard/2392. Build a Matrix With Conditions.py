class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        self.k = k
        row_order = self.sort(rowConditions)
        col_order = self.sort(colConditions)
        col_order = {x : i for i, x in enumerate(col_order)}
        grid = [[0 for i in range(k)] for i in range(k)]

        for i, x in enumerate(row_order):
            if not x in col_order:
                break
            j = col_order[x]
            grid[i][j] = x
        
        for i in grid:
            if not any(i):
                return []
        return grid
    
    def sort(self, relations):
        graph = defaultdict(list)
        degree = [0] * (self.k + 1)

        for prev, num in relations:
            graph[prev].append(num)
            degree[num] += 1
        
        q = deque()
        order = []

        for i in range(1, self.k+1):
            if not degree[i]:
                q.append(i)
        while q:
            curr = q.popleft()
            order.append(curr)
            for neighbor in graph[curr]:
                degree[neighbor] -= 1
                if not degree[neighbor]:
                    q.append(neighbor)

        return order if not any(degree) else []