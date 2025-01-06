# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.order = []
        self.inorder(root)
        n = len(self.order)
        node = self.create(root, 0, n-1)
        return node
    
    def create(self, root, left, right):
        if left > right:
            return

        mid = left + (right-left) // 2
        node = TreeNode(self.order[mid])
        node.left = self.create(node.left, left, mid-1)
        node.right = self.create(node.right, mid+1, right)
        return node

    def inorder(self, root):
        current = root
        stack = []

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
                
            current = stack.pop()
            self.order.append(current.val)
            current = current.right 