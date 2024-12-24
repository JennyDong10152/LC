class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        self.maxDiameter = 0
        self.search(0, -1, graph)
        return self.maxDiameter
    
    def search(self, node, parent, graph):
        deepest = 0
        secondDeepest = 0
        
        for neighbor in graph[node]:
            if neighbor == parent: 
                continue
            
            depth = self.search(neighbor, node, graph)

            if depth > deepest:
                secondDeepest = deepest
                deepest = depth
            elif depth > secondDeepest:
                secondDeepest = depth
        
        self.maxDiameter = max(self.maxDiameter, deepest + secondDeepest)
        return deepest + 1