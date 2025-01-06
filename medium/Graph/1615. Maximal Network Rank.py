class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        maxRank = 0
        graph = defaultdict(set)

        for city1, city2 in roads:
            graph[city1].add(city2)
            graph[city2].add(city1)
        
        for city1 in range(n):
            for city2 in range(city1+1, n):
                currentRank = len(graph[city1]) + len(graph[city2])
                if city2 in graph[city1]:
                    currentRank -= 1
                maxRank = max(maxRank, currentRank)
        return maxRank