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
        return self.build(preorder, inorder)
    
    def build(self, preorder, inorder):
        if inorder:
            idx = inorder.index(preorder.popleft())
            node = TreeNode(inorder[idx])
            node.left = self.build(preorder, inorder[:idx])
            node.right = self.build(preorder, inorder[idx+1:])
            return node