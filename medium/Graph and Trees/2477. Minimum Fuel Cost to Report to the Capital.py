class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        self.seats = seats
        for node1, node2 in roads:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        self.fuel = 0
        self.search(0, 0, graph)
        return self.fuel
    
    def search(self, node, prev, graph, people=1):
        for neighbor in graph[node]:
            if neighbor == prev:
                continue
            people += self.search(neighbor, node, graph)
        if node:
            self.fuel += (int(ceil(people/self.seats)))
        return people