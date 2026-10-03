class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        parent = [i for i in range(n+1)]
        graph = defaultdict(list)

        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        for i in range(1, n+1):
            root_i = self.find(parent, i)
            for enemy in graph[i]:
                root_enemy = self.find(parent, enemy)
                if root_i == root_enemy:
                    return False
                parent[enemy] = self.find(parent, graph[i][0])
        return True
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]