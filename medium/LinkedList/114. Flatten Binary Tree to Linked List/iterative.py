# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        dummy = current = root
        while current:
            if current.left:
                prev = current.left
                while prev.right:
                    prev = prev.right
                prev.right = current.right
                current.right = current.left
                current.left = None
            current = current.right
        return dummy