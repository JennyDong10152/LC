# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        self.subtree = []
        total = self.calculate(root)
        return total / 2 in self.subtree
    
    def calculate(self, node):
        if not node:
            return 0
        value = node.val
        if node.left:
            leftSum = self.calculate(node.left)
            value += leftSum
            self.subtree.append(leftSum)
        if node.right:
            rightSum = self.calculate(node.right)
            value += rightSum
            self.subtree.append(rightSum)
        return value