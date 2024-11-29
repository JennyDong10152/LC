class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr)-k

        if x < arr[0]:
            return arr[:k]
        if x > arr[-1]:
            return arr[k:]
        
        while left < right:
            mid = left + (right-left)//2
            midV = arr[mid]
            if x-midV > arr[mid+k]-x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left+k]
    