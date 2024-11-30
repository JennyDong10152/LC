class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        left = min(sweetness)
        right = sum(sweetness)

        while left <= right:
            mid = left + (right-left)//2
            if self.count(sweetness, mid, k+1):
                left = mid + 1
            else:
                right = mid - 1
        return right
    
    def count(self, sweetness, target, k):
        cur_sum = 0
        cnt = 0

        for s in sweetness:
            cur_sum += s
            if cur_sum >= target:
                cnt += 1
                cur_sum = 0
        return cnt >= k
            