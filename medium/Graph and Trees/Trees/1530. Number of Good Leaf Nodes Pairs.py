# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        self.pair = 0
        self.count(root, distance)
        return self.pair
    
    def count(self, node, distance):
        if not node:
            return []
        if not node.left and not node.right:
            return [1]
        
        left_distances = self.count(node.left, distance)
        right_distances = self.count(node.right, distance)

        for left_distance in left_distances:
            for right_distance in right_distances:
                if left_distance + right_distance <= distance:
                    self.pair += 1
        return [weight + 1 for weight in left_distances + right_distances]