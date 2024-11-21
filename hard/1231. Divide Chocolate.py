class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:

        left = min(sweetness)
        right = sum(sweetness) 

        while left <= right:
            mid = left + (right - left)//2
            if self.divide(sweetness, mid, k + 1):
                left = mid + 1 
            else:
                right = mid - 1
        return right

    def divide(self, nums, target, k):
        curr = 0
        cnt = 0

        for n in nums:
            curr += n
            if curr >= target:  
                cnt += 1
                curr = 0
        return cnt >= k