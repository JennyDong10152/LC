# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.i = 0
        self.ans = 0
        self.inorder(root, k)
        return self.ans
    
    def inorder(self, root, k):
        if not root:
            return
        
        self.inorder(root.left, k)
        self.i += 1

        if self.i == k:
            self.ans = root.val
            return
            
        self.inorder(root.right, k)
        