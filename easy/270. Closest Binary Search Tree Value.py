# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.dif = float("inf")
        self.node = float("inf")
        self.find(root, target)
        return self.node
    
    def find(self, root, target):
        if not root:
            return
        if abs(root.val-target) == self.dif:
            self.node = min(self.node, root.val)
        if abs(root.val-target) < self.dif:
            self.node = root.val
            self.dif = abs(root.val-target)
        if root.val >= target:
            self.find(root.left, target)
        if root.val <= target:
            self.find(root.right, target)