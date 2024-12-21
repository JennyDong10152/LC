class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) - 1
        self.paths = []
        self.search(0, [0], n, graph)
        return self.paths
        
    def search(self, current, path, n, graph):
        if current == n:
            self.paths.append(list(path))
            return
        
        for nextNode in graph[current]:
            path.append(nextNode)
            self.search(nextNode, path, n, graph)
            path.pop()