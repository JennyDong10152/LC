# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        lowestCommonAncestor = self.findLowestCommonAncestor(root, startValue, destValue)

        start_to_ancestor = []
        ancestor_to_des = []
        self.findPath(lowestCommonAncestor, startValue, start_to_ancestor)
        self.findPath(lowestCommonAncestor, destValue, ancestor_to_des)
        directions = ["U"]*len(start_to_ancestor) + ancestor_to_des

        return "".join(directions)

    def findPath(self, root, child, path):
        if not root:
            return False

        if root.val == child:
            return True

        path.append("L")
        if self.findPath(root.left, child, path):
            return True
        path.pop()

        path.append("R")
        if self.findPath(root.right, child, path):
            return True
        path.pop()
        return False

    def findLowestCommonAncestor(self, root, startValue, destValue):
        if not root:
            return None
        if root.val == startValue or root.val == destValue:
            return root
        
        left = self.findLowestCommonAncestor(root.left, startValue, destValue)
        right = self.findLowestCommonAncestor(root.right, startValue, destValue)

        if not left:
            return right
        if not right:
            return left
        return root