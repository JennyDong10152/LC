class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        
        for i in range(1, len(parent)):
            graph[parent[i]].append(i)
        
        self.ans = 0 
        self.search(graph, s, 0)
        
        return self.ans
     
    def search(self, graph, s, node):
        node_char = s[node]            
        longest = second_longest = 0
        
        for child in graph[node]:
            child_path = self.search(graph, s, child)
            if s[child] != node_char:                    
                if child_path >= longest:
                    second_longest = longest
                    longest = child_path 
                elif child_path > second_longest:
                    second_longest = child_path
                    
        self.ans = max(self.ans, 1 + longest + second_longest)        
        return 1 + longest