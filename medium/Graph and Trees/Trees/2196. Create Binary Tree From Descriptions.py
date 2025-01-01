# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        self.relation = defaultdict(list)
        all_nodes = set()
        children = set()

        for parent, child, isLeft in descriptions:
            self.relation[parent].append((child, isLeft))
            all_nodes.add(parent)
            all_nodes.add(child)
            children.add(child)
        root = (all_nodes - children).pop()
        return self.build(root)
    
    def build(self, node):
        root = TreeNode(node)
        for child, isLeft in self.relation[node]:
            if isLeft:
                root.left = self.build(child)
            if not isLeft:
                root.right = self.build(child)
        return root