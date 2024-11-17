# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftHeight = self.getLeftHeight(root)
        rightHeight = self.getRightHeight(root)
        if leftHeight == rightHeight:
            return 2 ** leftHeight - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
    def getLeftHeight(self, root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height

    def getRightHeight(self, root):
        height = 0
        while root:
            height += 1
            root = root.right
        return height