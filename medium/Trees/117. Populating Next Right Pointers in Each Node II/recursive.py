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
    def connect(self, root: 'Node') -> 'Node':
        node = self.traverse(root)
        return node
    
    def traverse(self, node):
        if not node:
            return None
        if node.left:
            node.left.next = node.right
        self.traverse(node.left)

        if node.right and node.next:
            if node.next.left:
                node.right.next = node.next.left
            elif node.next.right:
                node.right.next = node.next.right
        self.traverse(node.right)
        return node