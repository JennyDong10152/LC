class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7

        graph = defaultdict(list)
        for node1, node2, time in roads:
            graph[node1].append((node2, time))
            graph[node2].append((node1, time))

        distance = [float('inf')] * n
        distance[0] = 0
        ways = [0] * n
        ways[0] = 1

        heap = [(0, 0)]

        while heap:
            time, node = heappop(heap)
            for neighbor, neighbor_time in graph[node]:
                new_time = time + neighbor_time

                if new_time == distance[neighbor]:
                    ways[neighbor] += ways[node]
                elif new_time < distance[neighbor]:
                    distance[neighbor] = new_time
                    heappush(heap, (new_time, neighbor))
                    ways[neighbor] = ways[node]
        return ways[n-1] % MOD