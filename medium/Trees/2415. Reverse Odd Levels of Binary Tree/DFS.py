# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root.left, root.right, 0)
        return root
    
    def traverse(self, leftChild, rightChild, level):
        if leftChild is None or rightChild is None:
            return 
        
        if not level % 2:
            leftChild.val, rightChild.val = rightChild.val, leftChild.val
        self.traverse(leftChild.left, rightChild.right, level+1)
        self.traverse(leftChild.right, rightChild.left, level+1)