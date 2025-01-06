class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        for node1, node2 in roads:
            degree[node1] += 1
            degree[node2] += 1
        degree.sort()
        value = 1
        maxValue = 0
        for i in range(n):
            maxValue += value * degree[i]
            value += 1
        return maxValue