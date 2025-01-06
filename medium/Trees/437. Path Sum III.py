# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.count = 0
        self.sum = sum

        self.sums = defaultdict(int)
        self.preorder(root, 0)
        return self.count
    
    def preorder(self, node, prefix):
        if not node:
            return 

        prefix += node.val
        
        if prefix == self.sum:
            self.count += 1

        self.count += self.sums[prefix - self.sum]

        self.sums[prefix] += 1
        self.preorder(node.left, prefix)
        self.preorder(node.right, prefix)
        self.sums[prefix] -= 1