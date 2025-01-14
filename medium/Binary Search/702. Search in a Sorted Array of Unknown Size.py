class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left = 0
        right = 10**4

        while left <= right:
            mid = left + (right-left)//2
            midV = reader.get(mid)
            if midV == target:
                return mid
            elif midV == 2**31 - 1 or midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
        