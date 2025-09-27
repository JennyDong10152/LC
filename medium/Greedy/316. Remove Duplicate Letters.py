class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        visited = set()
        lastOccur = defaultdict(int)

        for idx, char in enumerate(s):
            lastOccur[char] = idx
        
        for idx, char in enumerate(s):
            if char not in visited:
                while stack and stack[-1] > char and lastOccur[stack[-1]] > idx:
                    visited.remove(stack.pop())
                visited.add(char)
                stack.append(char)
        return ''.join(stack)