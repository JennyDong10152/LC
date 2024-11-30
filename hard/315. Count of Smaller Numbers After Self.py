class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        cnt = []
        arr = []

        for n in reversed(nums):
            idx = self.search(arr, n)
            cnt.append(idx)
            arr.insert(idx, n)
        return cnt[::-1]
    
    def search(self, nums, target):
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left + (right-left)//2
            midV = nums[mid]
            if midV >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left