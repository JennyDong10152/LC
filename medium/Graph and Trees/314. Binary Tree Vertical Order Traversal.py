# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        order = defaultdict(list)
        queue = deque([(root, 0)])
        
        while queue:
            current, idx = queue.popleft()
            order[idx].append(current.val)
            if current.left:
                queue.append((current.left, idx-1))
            if current.right:
                queue.append((current.right, idx+1))
        return [order[x] for x in sorted(order.keys())]