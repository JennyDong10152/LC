# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        odd = False

        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()
                level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if odd:
                left = 0
                right = len(level)-1
                while left < right:
                    level[left].val, level[right].val = level[right].val, level[left].val
                    left += 1
                    right -= 1
            odd = not odd
        return root            