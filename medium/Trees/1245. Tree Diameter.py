class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        self.graph = defaultdict(list)
        for node1, node2 in edges:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)

        self.diameter = 0
        self.search(0, -1)
        return self.diameter
    
    def search(self, node, parent):
        deepest = secondDeepest = 0
        for child in self.graph[node]:
            if child == parent:
                continue
            depth = self.search(child, node)
            if depth >= deepest:
                secondDeepest = deepest
                deepest = depth
            elif depth >= secondDeepest:
                secondDeepest = depth
        self.diameter = max(self.diameter, deepest+secondDeepest)
        return 1 + deepest