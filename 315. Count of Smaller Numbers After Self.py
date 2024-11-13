class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums or len(nums)==1:
            return [0]

        n = len(nums)
        arr = []
        cnt = []

        for num in reversed(nums):
            idx = self.search(arr, num)
            cnt.append(idx)
            arr.insert(idx, num)
        return cnt[::-1]
    
    def search(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right-left)//2
            midV = arr[mid]
            if midV >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left
