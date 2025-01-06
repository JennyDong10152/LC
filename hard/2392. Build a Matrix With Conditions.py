class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        self.k = k
        rowRelation = self.build(rowConditions)
        colRelation = self.build(colConditions)

        if not rowRelation or not colRelation:
            return []
        colRelation = {num : idx for idx, num in enumerate(colRelation)}
        grid = [[0 for _ in range(k)] for _ in range(k)]

        for row, num in enumerate(rowRelation):
            if not num in colRelation:
                break
            col = colRelation[num]
            grid[row][col] = num
        
        for row in grid:
            if not any(row):
                return []
        return grid

    def build(self, condition):
        degree = [0] * (self.k+1)
        relation = defaultdict(list)

        for prev, second in condition:
            if not second in relation[prev]:
                relation[prev].append(second)
                degree[second] += 1
        
        queue = deque()
        order = []
        for num in range(1, self.k+1):
            if not degree[num]:
                queue.append(num)
        
        while queue:
            current = queue.popleft()
            order.append(current)
            for nextVal in relation[current]:
                degree[nextVal] -= 1
                if not degree[nextVal]:
                    queue.append(nextVal)
        return order if not any(degree) else []