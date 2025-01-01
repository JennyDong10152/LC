class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        self.preorder = preorder
        return self.verify([0], -inf, inf)
    
    def verify(self, current, min_limit, max_limit):
        if current[0] == len(self.preorder):
            return True
        
        root = self.preorder[current[0]]
        if not min_limit < root < max_limit:
            return False

        current[0] += 1
        left = self.verify(current, min_limit, root)
        right = self.verify(current, root, max_limit)
        return left or right