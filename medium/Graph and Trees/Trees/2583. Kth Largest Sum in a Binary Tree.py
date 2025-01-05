# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return []

        queue = deque([root])
        level_sums = []
        
        while queue:
            size = len(queue)
            level = 0
            for _ in range(size):
                node = queue.popleft()
                level += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_sums.append(level)
        level_sums.sort(reverse=True)
        return level_sums[k-1] if k <= len(level_sums) else -1