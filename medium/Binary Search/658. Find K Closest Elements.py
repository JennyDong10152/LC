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
            if x - arr[mid] <= arr[mid+k] - x:
                right = mid
            else:
                left = mid + 1
        return arr[left:left+k]