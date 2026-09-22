class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        lastOccur = defaultdict(int)
        visited = set()

        for idx, char in enumerate(s):
            lastOccur[char] = idx
        
        for idx, char in enumerate(s):
            if char not in visited:
                while stack and lastOccur[stack[-1]] > idx and stack[-1] > char:
                    visited.remove(stack.pop())
                visited.add(char)
                stack.append(char)
        return ''.join(stack)