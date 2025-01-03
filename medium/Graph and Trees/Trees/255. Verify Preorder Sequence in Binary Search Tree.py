class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        minLimit = -float("inf")
        stack = []

        for number in preorder:
            while stack and stack[-1] < number:
                minLimit = stack.pop()
            if number <= minLimit:
                return False
            stack.append(number)
        return True