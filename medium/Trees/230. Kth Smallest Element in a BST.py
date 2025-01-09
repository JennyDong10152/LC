# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.n = 0
        self.answer = 0
        self.inorder(root, k)
        return self.answer
    
    def inorder(self, node, k):
        if not node:
            return 
        
        self.inorder(node.left, k)

        self.n += 1
        if self.n == k:
            self.answer = node.val
            return 
        
        self.inorder(node.right, k)