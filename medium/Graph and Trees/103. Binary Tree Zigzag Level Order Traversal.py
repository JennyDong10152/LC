# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        order = []
        reverse = False
        while queue:
            size = len(queue)
            level_order = []
            for _ in range(size):
                current = queue.popleft()
                level_order.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            if reverse:
                level_order = level_order[::-1]
            order.append(level_order)
            reverse = not reverse
        return order