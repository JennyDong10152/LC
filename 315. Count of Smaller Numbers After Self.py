class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = []
        cnt = []

        for n in reversed(nums):
            idx = self.search(arr, n)
            cnt.append(idx)
            arr.insert(idx, n)
        return cnt[::-1]

    
    def search(self, arr, n):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right-left)//2
            midV = arr[mid]

            if midV >= n:
                right = mid - 1
            else:
                left = mid + 1
        return left