"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        self.first = self.prev = None
        self.convert(root)
        self.prev.right = self.first
        self.first.left = self.prev
        return self.first
    
    def convert(self, node):
        if not node:
            return 
        
        self.convert(node.left)
        if not self.prev:
            self.first = node
        else:
            node.left = self.prev
            self.prev.right = node
        self.prev = node
        self.convert(node.right)