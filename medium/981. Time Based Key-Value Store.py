class TimeMap:

    def __init__(self):
        self.maps = {} #key : [timestamp, value]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.maps:
            self.maps[key] = []
        self.maps[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.maps:
            return ""
        val = self.search(self.maps[key], timestamp)
        return val
    
    def search(self, lst, target):
        left = 0
        right = len(lst)-1
        
        while left <= right:
            mid = left + (right-left)//2
            midV = lst[mid][0]
            if midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return lst[right][1] if 0 <= right < len(lst) else ""