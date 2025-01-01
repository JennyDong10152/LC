# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        boundary = []
        if not self.isLeaf(root):
            boundary.append(root.val)
        boundary.extend(self.leftSide(root.left))
        boundary.extend(self.leaves(root))
        boundary.extend(self.rightSide(root.right))
        return boundary
    
    def isLeaf(self, root):
        if not root.left and not root.right:
            return True
        return False 

    def leftSide(self, node):
        if not node or self.isLeaf(node):
            return []

        if node.left:
            return [node.val] + self.leftSide(node.left)
        else:
            return [node.val] + self.leftSide(node.right)
        
    def rightSide(self, node):
        if not node or self.isLeaf(node):
            return []

        if node.right:
            return self.rightSide(node.right) + [node.val]
        else:
            return self.rightSide(node.left) + [node.val]
        
    def leaves(self, node):
        if not node:
            return []
        if self.isLeaf(node):
            return [node.val]
        left = self.leaves(node.left)
        right = self.leaves(node.right)
        return left + right