class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for start, destination in sorted(tickets, reverse=True):
            graph[start].append(destination)
        
        itinerary = []
        self.search(graph, "JFK", itinerary)
        return itinerary[::-1]
    
    def search(self, graph, airport, itinerary):
        while graph[airport]:
            self.search(graph, graph[airport].pop(), itinerary)
        itinerary.append(airport)