# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        self.summing(root, 0)
        return self.total
    
    def summing(self, node, number):
        if not node:
            return
        
        number = 10 * number + node.val
        if not node.left and not node.right:
            self.total += number
            return 
        
        self.summing(node.left, number)
        self.summing(node.right, number)