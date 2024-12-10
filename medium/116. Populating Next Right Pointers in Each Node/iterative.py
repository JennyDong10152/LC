"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        dummy = ListNode(0, root)
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)

            for i in range(size):
                if not i:
                    prev = queue.popleft()
                else:
                    cur = queue.popleft()
                    prev.next = cur
                    prev = cur
                    prev.next = None
                if prev.left:
                    queue.append(prev.left)
                if prev.right:
                    queue.append(prev.right)
        return dummy.next