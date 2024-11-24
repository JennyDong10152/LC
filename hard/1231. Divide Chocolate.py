class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        left = min(sweetness)
        right = sum(sweetness)

        while left <= right:
            mid = left + (right-left)//2
            if self.divide(sweetness, mid, k+1):
                left = mid + 1
            else:
                right = mid - 1
        return right
    
    def divide(self, sweetness, target, k):
        cnt = 0
        temp_sum = 0
        for s in sweetness:
            temp_sum += s
            if temp_sum >= target:
                cnt += 1
                temp_sum = 0
        return cnt >= k