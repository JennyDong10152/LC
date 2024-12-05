class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        obstacles = []
        results = []

        for query in queries:
            if query[0] == 1:
                x = query[1]
                idx_insert = self.search(obstacles, x)
                obstacles.insert(idx_insert, x)
            
            elif query[0] == 2:
                x, sz = query[1], query[2]
                can_place = self.canPlaceBlock(obstacles, x, sz)
                results.append(can_place)
        return results
    
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            midV = nums[mid]
            if midV >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def canPlaceBlock(self, obstacles, x, sz):
        if obstacles and obstacles[0] >= sz:
            return True
        
        for i in range(1, len(obstacles)):
            if obstacles[i] - obstacles[i - 1] >= sz:
                return True
        
        if x - obstacles[-1] >= sz:
            return True
        return False