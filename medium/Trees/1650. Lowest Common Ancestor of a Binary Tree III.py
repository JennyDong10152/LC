"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_depth = self.getDepth(p)
        q_depth = self.getDepth(q)

        for _ in range(p_depth - q_depth):
            p = p.parent
        for _ in range(q_depth - p_depth):
            q = q.parent
        
        while q != p:
            p = p.parent
            q = q.parent
        return q
    
    def getDepth(self, node):
        depth = 0
        while node:
            node = node.parent
            depth += 1
        return depth