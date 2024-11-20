class Solution:

    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        n = len(seq)
        self.seq = seq
        left = 0
        right = n // 2 
        ans = []  

        while left <= right:
            mid = left + (right-left)//2
            arr = [0] * n

            if self.test(mid, arr):
                ans = arr
                right = mid - 1
            else:
                left = mid + 1
        
        return ans

    def test(self, target, arr):
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
                    depth[curr] -= 1
                    arr[i] = curr
                    if depth[1] == 0: 
                        curr = 0

                maxDepth = max(maxDepth, depth[0], depth[1])
            return maxDepth <= target