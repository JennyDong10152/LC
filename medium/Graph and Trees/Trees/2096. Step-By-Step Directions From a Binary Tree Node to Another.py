# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        lowestCommonAncestor = self.findLowestCommonAncestor(root, startValue, destValue)
        start_to_root = []
        root_to_dest = []
        self.findPath(lowestCommonAncestor, startValue, start_to_root)
        self.findPath(lowestCommonAncestor, destValue, root_to_dest)

        directions = ["U"]*len(start_to_root) + root_to_dest
        return "".join(directions)
    
    def findPath(self, root, target, path):
        if not root:
            return False
        if root.val == target:
            return True
        
        path.append("L")
        if self.findPath(root.left, target, path):
            return True
        path.pop()

        path.append("R")
        if self.findPath(root.right, target, path):
            return True
        path.pop()
        return False
    
    def findLowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if root.val == p or root.val == q:
            return root
        left = self.findLowestCommonAncestor(root.left, p, q)
        right = self.findLowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root