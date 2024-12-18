"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, node: 'Optional[Node]') -> List[int]:
        array = []
        while node.prev:
            node = node.prev

        while node:
            array.append(node.val)
            node = node.next
        return array