class TimeMap:

    def __init__(self):
        self.maps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.maps[key].append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        if not key in self.maps:
            return ""
        
        return self.search(self.maps[key], timestamp)

    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            midV = nums[mid][0]

            if midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return nums[right][1] if 0 <= right < len(nums) else ""       