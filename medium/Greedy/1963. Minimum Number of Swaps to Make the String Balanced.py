class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        unmatched = 0

        for char in s:
            if char == '[':
                stack.append(char)
            else:
                if stack:
                    stack.pop()
                else:
                    unmatched += 1
        return (unmatched + 1) // 2