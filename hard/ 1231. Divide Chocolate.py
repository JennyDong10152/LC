class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:

        left = 1  
        right = sum(sweetness) 

        while left <= right:
            mid = left + (right - left)//2
            if self.divide(sweetness, mid, k + 1):
                left = mid + 1 
            else:
                right = mid - 1
                
        return right

    def divide(self, nums, target, pieces):
        curr = 0
        cnt = 0

        for sweet in nums:
            curr += sweet
            if curr >= target:  
                cnt += 1
                curr = 0  
        return cnt >= pieces