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

    def isBST(self, root, minLimit, maxLimit):
        if not root:
            return True
        if not minLimit < root.val < maxLimit:
            return False
        return self.isBST(root.left, minLimit, root.val) and self.isBST(root.right, root.val, maxLimit)
    
    def count(self, root):
        if not root:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)