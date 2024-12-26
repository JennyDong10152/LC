class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        self.graph = defaultdict(list)
        self.seats = seats
        self.fuel = 0
        for node1, node2 in roads:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)
        self.search(0, 0)
        return self.fuel
    
    def search(self, node, parent, people = 1):
        for neighbor in self.graph[node]:
            if neighbor == parent:
                continue
            people += self.search(neighbor, node)
        if node:
            self.fuel += int(ceil(people/self.seats))
        return people