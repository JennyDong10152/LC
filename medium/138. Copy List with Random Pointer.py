"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node = head
        maps = {None : None}

        while node:
            maps[node] = Node(node.val)
            node = node.next
        node = head
        while node:
            maps[node].random = maps[node.random]
            maps[node].next = maps[node.next]
            node = node.next
        return maps[head]