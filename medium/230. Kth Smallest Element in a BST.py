# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.ans = 0
        self.search(root, k)
        return self.ans
    
    def search(self, root, k):
        if not root:
            return
        self.search(root.left, k)
        self.cnt += 1
        if self.cnt == k:
            self.ans = root.val
            return 
        self.search(root.right, k)