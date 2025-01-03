# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.forest = []
        self.delete(root, set(to_delete))
        if not root.val in to_delete:
            self.forest.append(root)
        return self.forest
    
    def delete(self, node, to_delete):
        if not node:
            return None

        node.left = self.delete(node.left, to_delete)
        node.right = self.delete(node.right, to_delete)

        if node.val in to_delete:
            if node.left:
                self.forest.append(node.left)
            if node.right:
                self.forest.append(node.right)
            return None
        return node