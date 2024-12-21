class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for start, end, weight in times:
            graph[start].append((end, weight))
        
        heap = [(0, k)]  # (time, node)
        distance = {}
        
        while heap:
            time, node = heapq.heappop(heap)
            if node in distance:
                continue
            
            distance[node] = time
            for neighbor, weight in graph[node]:
                if neighbor not in distance:
                    heapq.heappush(heap, (time + weight, neighbor))
        
        return max(distance.values()) if len(distance) == n else -1