# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.trees = []
        root = self.delete(root, set(to_delete))
        if root:
            self.trees.append(root)
        return self.trees
    
    def delete(self, root, to_delete):
        if not root:
            return None
        
        root.left = self.delete(root.left, to_delete)
        root.right = self.delete(root.right, to_delete)

        if root.val in to_delete:
            if root.left:
                self.trees.append(root.left)
            if root.right:
                self.trees.append(root.right)
            return None
        return root