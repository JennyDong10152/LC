# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.check(root.left, root.right)

    def check(self, leftTree, rightTree):
        if not leftTree and not rightTree:
            return True
        if (not leftTree or not rightTree) or (leftTree.val != rightTree.val):
            return False
        return self.check(leftTree.right, rightTree.left) and self.check(leftTree.left, rightTree.right)