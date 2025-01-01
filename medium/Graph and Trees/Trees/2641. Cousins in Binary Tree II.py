# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_sums = self.calculate(root)
        self.replace(root, level_sums)
        return root

    def replace(self, root, level_sums):
        root.val = 0
        queue = deque([root])
        idx = 1
        
        while queue:
            size = len(queue)
            for _ in range(size):
                current = queue.popleft()
                sibling = (current.left.val if current.left else 0) + (current.right.val if current.right else 0)
                if current.left:
                    current.left.val = level_sums[idx] - sibling
                    queue.append(current.left)
                if current.right:
                    current.right.val = level_sums[idx] - sibling
                    queue.append(current.right)
            idx += 1

    def calculate(self, root):
        level_sums = []
        queue = deque([root])

        while queue:
            size = len(queue)
            level = 0
            for _ in range(size):
                current = queue.popleft()
                level += current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            level_sums.append(level)
        return level_sums