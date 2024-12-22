# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.value = 0
        self.calculate(root)
        return root
    
    def calculate(self, root):
        if not root:
            return 0
        self.calculate(root.right)
        self.value += root.val
        root.val = self.value
        self.calculate(root.left)