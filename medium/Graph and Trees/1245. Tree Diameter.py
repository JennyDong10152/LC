class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        
        self.graph = defaultdict(list)
        for node1, node2 in edges:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)
        self.maxDiameter = 0
        self.search(0, -1)
        return self.maxDiameter
    
    def search(self, current, parent):
        deepest = 0
        secondDeepest = 0

        for neighbor in self.graph[current]:
            if neighbor == parent:
                continue
            depth = self.search(neighbor, current)
            if depth >= deepest:
                secondDeepest = deepest
                deepest = depth
            elif depth > secondDeepest:
                secondDeepest = depth
        self.maxDiameter = max(self.maxDiameter, deepest+secondDeepest)
        return 1 + deepest