class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        degree = [0] * n

        for start, end in edges:
            degree[end] += 1
        
        roots = []
        for i in range(n):
            if not degree[i]:
                roots.append(i)
        return roots