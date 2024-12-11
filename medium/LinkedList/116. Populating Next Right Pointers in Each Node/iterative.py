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
        if not root:
            return None
        head = root
        queue = deque([head])

        while queue:
            size = len(queue)
            prev = None
            for _ in range(size):
                curr = queue.popleft()
                if prev is None:
                    prev = curr
                else:
                    prev.next = curr
                    prev = curr
                    prev.next = None
                if prev.left:
                    queue.append(prev.left)
                if prev.right:
                    queue.append(prev.right)
        return root