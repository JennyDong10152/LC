# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        relation = defaultdict(list)
        all_nodes = set()
        children = set()

        for parent, child, isLeft in descriptions:
            relation[parent].append((child, isLeft))
            all_nodes.add(parent)
            all_nodes.add(child)
            children.add(child)

        root = (all_nodes - children).pop()
        return self.build(root, relation)

    def build(self, value, relation):
        node = TreeNode(value)

        if value in relation:
            for child, isLeft in relation[value]:
                if isLeft:
                    node.left = self.build(child, relation)
                else:
                    node.right = self.build(child, relation)
        return node