# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        return self.convert(s, 0)[0]
    
    def getNumber(self, s, index):
        isNegative = False
        
        if s[index] == '-':
            isNegative = True
            index = index + 1
        
        number = 0
        while index < len(s) and s[index].isdigit():
            number = number * 10 + int(s[index])
            index += 1
        
        return number if not isNegative else -number, index
            
    def convert(self, s, index):
        if index == len(s):
            return None, index
        value, index = self.getNumber(s, index)
        node = TreeNode(value)

        if index < len(s) and s[index] == '(':
            node.left, index = self.convert(s, index + 1)
        
        if node.left and index < len(s) and s[index] == '(':
            node.right, index = self.convert(s, index + 1)
        
        return node, index + 1 if index < len(s) and s[index] == ')' else index