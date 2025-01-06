class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        xDict = {}
        yDict = {}
        parent = [i for i in range(len(stones))]
        edges = []
        answer = 0

        for i, [stoneX, stoneY] in enumerate(stones):
            if stoneX in xDict:
                edges.append((i, xDict[stoneX]))
            else:
                xDict[stoneX] = i
            if stoneY in yDict:
                edges.append((i, yDict[stoneY]))
            else:
                yDict[stoneY] = i
        
        for x, y in edges:
            answer += self.union(parent, x, y)
        return answer
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_y] = root_x
            return 1
        return 0
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]