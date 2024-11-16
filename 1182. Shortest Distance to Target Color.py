class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        if not colors or not queries:
            return []
        ans = []
        maps = dict()
        for i, c in enumerate(colors):
            if not c in maps:
                maps[c] = []
<<<<<<< Updated upstream
            maps[c].append(i)
        for i, c in queries:
=======
            maps[c].append(idx)        
        for idx, c in queries:
>>>>>>> Stashed changes
            if not c in maps:
                ans.append(-1)
            else:
                ans.append(self.search(i, maps[c]))
        return ans
    
    
    def search(self, target, nums):
        left = 0
        right = len(nums)-1
        diff = float('inf')

        while left <= right:
            mid = left + (right-left)//2
            midV = nums[mid]
            diff = min(diff, abs(midV-target))
            if midV == target:
                return 0
            if midV > target:
                right = mid-1
            else:
<<<<<<< Updated upstream
                left = mid+1
        return diff
=======
                left = mid + 1
        return diff
>>>>>>> Stashed changes
