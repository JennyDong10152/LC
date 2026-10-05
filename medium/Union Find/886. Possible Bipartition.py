class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        parent = [i for i in range(n+1)]
        graph = defaultdict(list)

        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        for person in range(1, n+1):
            root_person = self.find(parent, person)
            for enemy in graph[person]:
                root_enemy = self.find(parent, enemy)
                if root_person == root_enemy:
                    return False
                parent[enemy] = self.find(parent, graph[person][0])
        return True
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]