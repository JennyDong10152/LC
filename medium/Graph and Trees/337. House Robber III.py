# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        money = self.robbing(root)
        return max(money)
    
    def robbing(self, root):
        if not root:
            return [0,0]
        left = self.robbing(root.left)
        right = self.robbing(root.right)
        rob = root.val + left[1] + right[1]
        notRob = max(left) + max(right)
        return [rob, notRob]