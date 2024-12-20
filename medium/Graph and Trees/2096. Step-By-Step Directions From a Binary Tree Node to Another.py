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
        self.findPath(lowestCommonAncestor, startValue, start_to_ancestor)
        ancestor_to_des = []
        self.findPath(lowestCommonAncestor, destValue, ancestor_to_des)
        print(ancestor_to_des)

        directions = ["U"]*len(start_to_ancestor) + ancestor_to_des
        return "".join(directions)

    def findPath(self, node, target, path):
        if node is None:
            return False
        if node.val == target:
            return True

        path.append("L")
        if self.findPath(node.left, target, path):
            return True
        path.pop()

        path.append("R")
        if self.findPath(node.right, target, path):
            return True
        path.pop()
        return False
    
    def findLowestCommonAncestor(self, node, startValue, destValue):
        if not node:
            return None
        
        if node.val == startValue or node.val == destValue:
            return node
        
        left = self.findLowestCommonAncestor(node.left, startValue, destValue)
        right = self.findLowestCommonAncestor(node.right, startValue, destValue)

        if not left:
            return right
        elif not right:
            return left
        return node