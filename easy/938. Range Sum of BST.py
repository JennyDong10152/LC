# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total = 0
        self.summing(root, low, high)
        return self.total

    def summing(self, node, low, high):
        if not node:
            return
        if low <= node.val <= high:
            self.total += node.val
        if low < node.val:
            self.summing(node.left, low, high)
        if high > node.val:
            self.summing(node.right, low, high)