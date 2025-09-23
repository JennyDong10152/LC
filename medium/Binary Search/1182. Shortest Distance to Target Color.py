class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        maps = defaultdict(list)
        for idx, color in enumerate(colors):
            maps[color].append(idx)

        ans = []
        for idx, color in queries:
            if color not in maps:
                ans.append(-1)
            else:
                ans.append(self.find(maps[color], idx))
        return ans
    
    def find(self, arr, target):
        left = 0
        right = len(arr) - 1
        minDiff = float("inf")

        while left <= right:
            mid = left + (right -left) // 2
            midV = arr[mid]
            minDiff = min(minDiff, abs(midV - target))
            if not minDiff:
                return 0
            if midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return minDiff