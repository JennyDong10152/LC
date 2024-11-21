class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        self.seq = seq
        n = len(seq)
        left = 0
        right = n//2
        ans = []

        while left <= right:
            mid = left + (right-left)//2
            arr = [0] * n
            if self.test(arr, mid):
                ans = arr
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def test(self, arr, target):
        depth = [0, 0]
        curr = 0
        maxDepth = 0

        for i, c in enumerate(self.seq):
            if c == '(':
                if depth[0] == target:
                    curr = 1
                depth[curr] += 1
                arr[i] = curr
            else:
                arr[i] = curr
                depth[curr] -= 1
                if depth[1] == 0:
                    curr = 0
            maxDepth = max(maxDepth, depth[0], depth[1])
        return maxDepth <= target