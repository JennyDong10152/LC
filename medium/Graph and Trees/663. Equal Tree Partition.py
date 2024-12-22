# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        self.total = 0
        self.subtree = []
        self.total = self.sumTrees(root)
        return self.total/2 in self.subtree
    
    def sumTrees(self, node):
        value = node.val
        if node.left:
            leftSum = self.sumTrees(node.left)
            value += leftSum
            self.subtree.append(leftSum)
        if node.right:
            rightSum = self.sumTrees(node.right)
            value += rightSum
            self.subtree.append(rightSum)
        return value