# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder, postorder)
    
    def build(self, preorder, postorder):
        if preorder:
            if len(preorder) == 1:
                return TreeNode(postorder.pop())

            node = TreeNode(postorder.pop())
            idx = preorder.index(postorder[-1])

            node.right = self.build(preorder[idx:], postorder)
            node.left = self.build(preorder[1:idx], postorder)
            return node
