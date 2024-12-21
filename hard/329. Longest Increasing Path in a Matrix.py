class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        degree = [[0] * n for _ in range(m)]  #how many nearby cubes are smaller
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for i in range(m):
            for j in range(n):
                for di, dj in direction:
                    new_i = i + di
                    new_j = j + dj
                    if 0 <= new_i < m and 0 <= new_j < n and matrix[new_i][new_j] < matrix[i][j]:
                        degree[i][j] += 1
 
        queue = deque([[i, j] for i in range(m) for j in range(n) if not degree[i][j]])

        max_path = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                for di, dj in direction:
                    new_i = i + di
                    new_j = j + dj
                    if 0 <= new_i < m and 0 <= new_j < n and matrix[new_i][new_j] > matrix[i][j]:
                        degree[new_i][new_j] -= 1
                        if not degree[new_i][new_j]:
                            queue.append((new_i, new_j))
            max_path += 1
        return max_path