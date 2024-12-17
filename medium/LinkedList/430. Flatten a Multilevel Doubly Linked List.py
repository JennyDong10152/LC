"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.flatting(head)
        return head
    
    def flatting(self, node):
        if not node:
            return None
        if not node.child and not node.next:
            return node
        if not node.child:
            return self.flatting(node.next)
        
        childTail = self.flatting(node.child)
        nextNode = node.next
        childTail.next = nextNode
        if nextNode:
            nextNode.prev = childTail
        node.next = node.child
        node.child.prev = node
        node.child = None
        return self.flatting(nextNode) if nextNode else childTail 