class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x < arr[0]:
            return arr[:k]
        if x > arr[-1]:
            return arr[k:]
        
        left = 0
        right = len(arr)-k

        while left < right:
            mid = left + (right - left)//2
            midV = arr[mid]
            if arr[mid+k] - x >= x - midV:
                right = mid
            else:
                left = mid + 1
        return arr[left : left + k]