class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        temp = intervals[0]
        ans = []

        for start, end in intervals[1:]:
            if temp[1] >= start:
                temp[1] = max(temp[1], end)
            else:
                ans.append(temp)
                temp = [start, end]
        ans.append(temp)
        return ans