"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        node = self.traverse(root)
        return node
    
    def traverse(self, node):
        if not node:
            return 
        
        if node.left:
            node.left.next = node.right
            self.traverse(node.left)
        if node.right and node.next and node.next.left:
            node.right.next = node.next.left
        self.traverse(node.right)
        return node