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
        self.first.left = self.prev
        self.prev.right = self.first
        return self.first
    
    def convert(self, node):
        if not node:
            return None

        self.convert(node.left)

        if not self.prev:
            self.first = node
        else:
            self.prev.right = node
            node.left = self.prev

        self.prev = node
        self.convert(node.right)