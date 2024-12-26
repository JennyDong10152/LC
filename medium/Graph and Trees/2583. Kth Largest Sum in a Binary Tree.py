# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sums = []
        queue = deque([root])
        
        while queue:
            size = len(queue)
            temp_sum = 0
            for _ in range(size):
                current = queue.popleft()
                temp_sum += current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            level_sums.append(temp_sum)
        level_sums.sort(reverse = True)

        return level_sums[k-1] if k <= len(level_sums) else -1