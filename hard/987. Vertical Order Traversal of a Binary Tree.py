# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        order = defaultdict(list)
        queue = deque([(root, 0, 0)])

        while queue:
            node, row, col = queue.popleft()
            order[col].append((row, node.val))
            if node.left:
                queue.append((node.left, row+1, col-1))
            if node.right:
                queue.append((node.right, row+1, col+1))
        order = [order[x] for x in sorted(order.keys())]

        for i in range(len(order)):
            temp_list = order[i]
            temp_list.sort()
            order[i] = [x[1] for x in temp_list]
        return order