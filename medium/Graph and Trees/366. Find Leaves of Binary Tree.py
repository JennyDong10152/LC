# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.leaves = defaultdict(list)
        self.find(root)
        return list(self.leaves.values())
    
    def find(self, root):
        if not root:
            return 0
        left = self.find(root.left)
        right = self.find(root.right)
        level = 1 + max(left, right)
        self.leaves[level].append(root.val)
        return level