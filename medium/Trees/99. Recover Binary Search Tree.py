# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = self.second = None
        self.prev = TreeNode(-float("inf"))
        
        self.traverse(root)
        
        self.first.val, self.second.val = self.second.val, self.first.val

    def traverse(self, node):
        if not node:
            return 
        self.traverse(node.left)
        if not self.first and self.prev.val >= node.val:
            self.first = self.prev
        if self.first and self.prev.val >= node.val:
            self.second = node
        self.prev = node
        self.traverse(node.right)
        