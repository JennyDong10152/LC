# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        self.distribute(root)
        return self.moves
    
    def distribute(self, node):
        if not node:
            return 0
        left = self.distribute(node.left)
        right = self.distribute(node.right)
        self.moves += abs(left) + abs(right)
        return node.val-1 + left + right