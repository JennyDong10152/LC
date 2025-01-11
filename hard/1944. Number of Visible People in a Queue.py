class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = [0] * n
        stack = []

        for idx, height in enumerate(reversed(heights)):
            while stack and stack[-1] < height:
                stack.pop()
                answer[idx] += 1
            if stack:
                answer[idx] += 1
            stack.append(height)
        return answer[::-1]