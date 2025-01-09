class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        reference = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in reference:
                bracket = stack.pop() if stack else '#'
                if bracket != reference[char]:
                    return False
            else:
                stack.append(char)
        return not stack