class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0]*n
        for node1, node2 in roads:
            degree[node1] += 1
            degree[node2] += 1
        
        degree.sort()
        value = 1
        total = 0
        for d in degree:
            total += value * d
            value += 1
        return total