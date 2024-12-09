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
    
    def traverse(self, root):
        if not root:
            return None
        
        if root.left:
            root.left.next = root.right
            self.traverse(root.left)
        if root.right and root.next and root.next.left:
            root.right.next = root.next.left
        self.traverse(root.right)
        return root