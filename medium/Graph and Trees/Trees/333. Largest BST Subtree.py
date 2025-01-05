# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if self.isBST(root, -float("inf"), float("inf")):
            return self.count(root)
        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))
    
    def isBST(self, node, minLimit, maxLimit):
        if not node:
            return True
        if not minLimit < node.val < maxLimit:
            return False
        return self.isBST(node.left, minLimit, node.val) and self.isBST(node.right, node.val, maxLimit)
    
    def count(self, node):
        if not node:
            return 0
        return 1 + self.count(node.left) + self.count(node.right)