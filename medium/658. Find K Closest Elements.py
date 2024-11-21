class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if arr[0] > x:
            return arr[:k]
        if arr[-1] < x:
            return arr[k:]

        left = 0
        right = len(arr)-k
        while left < right:
            mid = left + (right-left)//2
            midV = arr[mid]
            if x-midV > arr[mid+k]-x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left+k]
