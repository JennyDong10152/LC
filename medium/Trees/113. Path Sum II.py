# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.paths = []
        self.recurse(root, targetSum, [])
        return self.paths
    
    def recurse(self, node, target, path):
        if not node:
            return None

        path.append(node.val)
        if self.isLeaf(node) and sum(path) == target:
            self.paths.append(list(path))
        else:
            self.recurse(node.left, target, path)
            self.recurse(node.right, target, path)
        path.pop()

    def isLeaf(self, node):
        return not node.left and not node.right