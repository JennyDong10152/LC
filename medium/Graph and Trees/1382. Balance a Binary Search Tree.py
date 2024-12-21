# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        order = []
        self.inorder(root, order)
        n = len(order)
        node = self.create(root, order, 0, n-1)
        return node
    
    def create(self, root, order, left, right):
        if left > right:
            return
        mid = left + (right-left)//2
        node = TreeNode(order[mid])
        node.left = self.create(node.left, order, left, mid-1)
        node.right = self.create(node.right, order, mid+1, right)
        return node

    def inorder(self, root, order):
        if not root:
            return
        self.inorder(root.left, order)
        order.append(root.val)
        self.inorder(root.right, order)