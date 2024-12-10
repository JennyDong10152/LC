"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        node = head
        memory = {None: None}

        while node:
            memory[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            memory[node].random = memory[node.random]
            memory[node].next = memory[node.next]
            node = node.next
        return memory[head]