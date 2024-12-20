# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.find(root)
        
    def find(self, root):
        if not root:
            return 0
        left = self.find(root.left)
        right = self.find(root.right)
        level = max(left, right) + 1
        return level