class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        temp = intervals[0]
        answer = []

        for [start, end] in intervals[1:]:
            if start <= temp[1]:
                temp[1] = max(temp[1], end)
            else:
                answer.append(temp)
                temp = [start, end]
        answer.append(temp)
        return answer

