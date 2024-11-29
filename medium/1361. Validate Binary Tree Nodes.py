class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = [i for i in range(n)]
        
        for i in range(n):
            parent_root = self.find(parent, i)
            children = [leftChild[i], rightChild[i]]
            for child in children:
                if child == -1:
                    continue
                child_root = self.find(parent, child)
                if child_root == parent_root or child_root != child:
                    return False
                parent[child_root] = parent_root

        root_count = sum(1 for i in range(n) if self.find(parent, i) == i)
        return root_count == 1
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]
    #reviewed