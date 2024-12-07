class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        maps = {}
        for i, c in enumerate(colors):
            if not c in maps:
                maps[c] = []
            maps[c].append(i)
        
        ans = []
        for i, c in queries:
            if not c in maps:
                ans.append(-1)
            else:
                ans.append(self.search(maps[c], i))
        return ans
    
    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        min_diff = float("inf")

        while left <= right:
            mid = left + (right-left)//2
            midV = nums[mid]
            min_diff = min(min_diff, abs(midV-target))
            if not min_diff:
                return 0
            if midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return min_diff
