class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        xDict = {}
        yDict = {}
        parent = [i for i in range(len(stones))]

        edges = []
        ans = 0

        for i, [stoneX, stoneY] in enumerate(stones):
            if stoneX in xDict:
                edges.append([xDict[stoneX], i])
            else:
                xDict[stoneX] = i
            if stoneY in yDict:
                edges.append([yDict[stoneY], i])
            else:
                yDict[stoneY] = i
        
        for x, y in edges:
            ans += self.union(parent, x, y)
        return ans
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y
            return 1
        return 0
    
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]