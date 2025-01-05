class Solution:
    def isPreorder(self, nodes: List[List[int]]) -> bool:
        stack = [nodes[0][0]]
        for node, parent in nodes[1:]:
            while stack and stack[-1] != parent:
                stack.pop()
            if not stack:
                return False
            stack.append(node)
        return True