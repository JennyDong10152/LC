# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        return self.recurse(root)

    def recurse(self, node):
        if not node.left:
            return node
        root = self.recurse(node.left)
        node.left.left = node.right
        node.left.right = node
        node.left = node.right = None
        return root