"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        newNode = Node(insertVal)
        if not head:
            newNode.next = newNode
            return newNode
        
        prev = head
        current = head.next
        while prev.next != head:
            if prev.val <= insertVal <= current.val:
                break
            if prev.val > current.val and insertVal < current.val:
                break
            if prev.val > current.val and insertVal > prev.val:
                break
            prev = current
            current = current.next
        prev.next = newNode
        newNode.next = current
        return head
