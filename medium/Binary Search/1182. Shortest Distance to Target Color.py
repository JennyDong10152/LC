class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        maps = defaultdict(list)
        for idx, color in enumerate(colors):
            maps[color].append(idx)
        
        answer = []
        for idx, color in queries:
            if not color in maps:
                answer.append(-1)
            else:
                answer.append(self.search(maps[color], idx))
        return answer
    
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        minDiff = float("inf")

        while left <= right:
            mid = left + (right - left) // 2
            midV = nums[mid]
            minDiff = min(minDiff, abs(midV-target))
            if not minDiff:
                return 0
            if midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return minDiff