# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = -float("inf")
        self.maxPath(root)
        return self.maxSum
    
    def maxPath(self, node):
        if not node:
            return 0

        left = max(0, self.maxPath(node.left))
        right = max(0, self.maxPath(node.right))
        current = node.val + left + right
        self.maxSum = max(self.maxSum, current)
        return max(left, right) + node.val