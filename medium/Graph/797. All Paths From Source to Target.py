class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.n = len(graph)-1
        self.graph = graph
        self.paths = []
        self.search(0, [0])
        return self.paths
    
    def search(self, current, path):
        if current == self.n:
            self.paths.append(list(path))
            return
        for neighbor in self.graph[current]:
            path.append(neighbor)
            self.search(neighbor, path)
            path.pop()