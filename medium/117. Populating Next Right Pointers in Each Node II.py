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
        if not root:
            return None
        
        dummy = ListNode(0, root)
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            prev = None
            for _ in range(size):
                if not prev:
                    prev = queue.popleft()
                else:
                    curr = queue.popleft()
                    prev.next = curr
                    prev = curr
                    prev.next = None
                if prev.left:
                    queue.append(prev.left)
                if prev.right:
                    queue.append(prev.right)
        return dummy.next