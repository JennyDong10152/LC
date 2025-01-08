class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        degree = [0] * n
        for win, lose in edges:
            degree[lose] += 1
            
        winner = set()
        for i in range(n):
            if not degree[i]:
                winner.add(i)
        return winner.pop() if len(winner) == 1 else -1