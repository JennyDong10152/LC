class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        self.k= k
        row_order = self.sort(rowConditions)
        col_order = self.sort(colConditions)

        col_order = {x : i for i, x in enumerate(col_order)}
        ans = [[0]*k for _ in range(k)]

        for i, x in enumerate(row_order):
            if x not in col_order:
                break
            j = col_order[x]
            ans[i][j] = x

        for i in ans:
            if not any(i):
                return []
        return ans
    
    def sort(self, relations):
        graph = defaultdict(list)
        degree = [0] * (self.k + 1)
        for prev, node in relations:
            graph[prev].append(node)
            degree[node] += 1
        
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