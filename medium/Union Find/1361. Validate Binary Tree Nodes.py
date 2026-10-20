class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        parent = [i for i in range(n)]

        for node in range(n):
            children = [leftChild[node], rightChild[node]]
            node_root = self.find(parent, node)
            for child in children:
                if child != -1:
                    child_root = self.find(parent, child)
                    if child_root == node_root or child_root != child:
                        return False
                    parent[child] = node_root

        root_count = set()
        for node in range(n):
            node_root = self.find(parent, node)
            root_count.add(node_root)
        return len(root_count) == 1
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]