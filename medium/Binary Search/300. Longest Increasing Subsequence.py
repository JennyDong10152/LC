class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        array = []
        for num in nums:
            idx = self.search(array, num)
            if idx < len(array):
                array[idx] = num
            else:
                array.append(num)
        return len(array)
    
    def search(self, array, target):
        left = 0
        right = len(array) - 1

        while left <= right:
            mid = left + (right - left) // 2
            midV = array[mid]

            if midV >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left