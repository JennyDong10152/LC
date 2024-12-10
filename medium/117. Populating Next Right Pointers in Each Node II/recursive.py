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
    
    def traverse(self, root):
        if not root:
            return None
        if root.left:
            root.left.next = root.right
        self.traverse(root.left)
        
        if root.right and root.next:
            if root.next.left:
                root.right.next = root.next.left
            elif root.next.right:
                root.right.next = root.next.right
        self.traverse(root.right)
        return root