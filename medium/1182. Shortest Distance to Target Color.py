class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        if not colors or not queries:
            return []
        
        ans = []
        maps = dict()
        for i, c in enumerate(colors):
            if not c in maps:
                maps[c] = []
            maps[c].append(i)
        
        for i, c in queries:
            if not c in maps:
                ans.append(-1)
            else:
                ans.append(self.search(maps[c], i))
        return ans
    
    def search(self, nums, target):
        diff = float("inf")
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left + (right-left)//2
            midV = nums[mid]
            diff = min(diff, abs(midV-target))
            if midV == target:
                return diff
            elif midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return diff       