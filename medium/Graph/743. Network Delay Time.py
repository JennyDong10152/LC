class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for start, end, weight in times:
            graph[start].append((weight, end))
        
        heap = [(0, k)]  # (time, node)
        distance = {}
        
        while heap:
            time, node = heapq.heappop(heap)
            if node in distance:
                continue
            distance[node] = time
            for weight, neighbor in graph[node]:
                heapq.heappush(heap, (time + weight, neighbor))
        
        return max(distance.values()) if len(distance) == n else -1