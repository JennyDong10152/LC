class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        visited = {}
        
        heap = [(0, start[0], start[1])]
        while heap:
            weight, x, y = heappop(heap)
            if (x, y) in visited and visited[(x, y)] <= weight:
                continue
            if x == target[0] and y == target[1]:
                return weight

            visited[(x, y)] = weight
            direct = self.distance(x, y, target[0], target[1])
            heappush(heap, (weight + direct, target[0], target[1]))
            for x1, y1, x2, y2, cost in specialRoads:
                passage = self.distance(x, y, x1, y1) + cost
                heappush(heap, (weight + passage, x2, y2))
        return -1
    
    def distance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)