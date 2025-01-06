# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)
        preorder = deque(preorder)
        return self.build(inorder, preorder)
    
    def build(self, inorder, preorder):
        if inorder:
            idx = inorder.index(preorder.popleft())
            root = TreeNode(inorder[idx])
            root.left = self.build(inorder[:idx], preorder)
            root.right = self.build(inorder[idx+1:], preorder)
            return root