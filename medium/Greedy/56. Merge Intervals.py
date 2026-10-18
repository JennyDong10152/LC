class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        temp = intervals[0]
        ans = []

        for [start, end] in intervals[1:]:
            if start <= temp[1]:
                temp[1] = max(end, temp[1])
            else:
                ans.append(temp)
                temp = [start, end]
        ans.append(temp)
        return ans