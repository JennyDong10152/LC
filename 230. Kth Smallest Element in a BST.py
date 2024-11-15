# Definition for a binary tree node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return
        self.ans = 0
        self.cnt = 0
        self.inorder(root, k)
        return self.ans
    
    def inorder(self, root, k):
        if not root:
            return
        self.inorder(root.left, k)
        self.cnt += 1
        if self.cnt == k:
            self.ans = root.val
            return 
        self.inorder(root.right, k)