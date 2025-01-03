# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.paths = []
        self.traverse(root, [])
        return self.paths
    
    def traverse(self, node, path):
        if not node:
            return
        path.append(str(node.val))
        if not node.left and not node.right:
            self.paths.append("->".join(path))
        else:
            self.traverse(node.left, path)
            self.traverse(node.right, path)
        path.pop()