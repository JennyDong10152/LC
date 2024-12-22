class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        degree = [0] * n
        for win, lose in edges:
            degree[lose] += 1
        winners = []
        for i in range(n):
            if not degree[i]:
                winners.append(i)
        return -1 if len(winners) != 1 else winners[0]