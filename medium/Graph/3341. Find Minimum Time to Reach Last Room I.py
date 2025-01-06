class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])
        minTime = [[float("inf") for _ in range(n)] for _ in range(m)]
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        minTime[0][0] = 0
        heap = [(0, 0, 0)]

        while heap:
            weight, i, j = heappop(heap)
            if i == m-1 and j == n-1:
                return weight
            for di, dj in direction:
                new_i = i + di
                new_j = j + dj
                if 0 <= new_i < m and 0 <= new_j < n:
                    newTime = max(weight, moveTime[new_i][new_j]) + 1
                    if minTime[new_i][new_j] > newTime:
                        minTime[new_i][new_j] = newTime
                        heappush(heap, (newTime, new_i, new_j))
        return 0