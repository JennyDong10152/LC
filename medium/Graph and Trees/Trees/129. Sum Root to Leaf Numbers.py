# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        self.sum(root, 0)
        return self.total
    
    def sum(self, node, number):
        if not node:
            return
        
        number = 10 * number + node.val
        if not node.left and not node.right:
            self.total += number
            return 

        self.sum(node.left, number)
        self.sum(node.right, number)