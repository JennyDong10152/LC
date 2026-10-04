class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastOccur = defaultdict(int)
        for idx, char in enumerate(s):
            lastOccur[char] = idx
        
        stack = []
        visited = set()
        for idx, char in enumerate(s):
            if char not in visited:
                while stack and lastOccur[stack[-1]] > idx and char < stack[-1]:
                    visited.remove(stack.pop())
                visited.add(char)
                stack.append(char)
        return ''.join(stack)