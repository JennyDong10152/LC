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
        answer = []
        for i in self.leaves:
            answer.append(self.leaves[i])
        return answer
    
    def find(self, node):
        if not node:
            return 0
        left = self.find(node.left)
        right = self.find(node.right)
        level = max(left, right)+1
        self.leaves[level].append(node.val)
        return level