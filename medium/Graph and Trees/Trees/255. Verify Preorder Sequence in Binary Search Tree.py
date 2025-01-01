class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        min_limit = -float("inf")
        stack = []
        
        for number in preorder:
            while stack and stack[-1] < number:
                min_limit = stack.pop()
                
            if number <= min_limit:
                return False
            
            stack.append(number)
        return True