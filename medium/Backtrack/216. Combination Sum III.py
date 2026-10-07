class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        self.ans = []
        self.backtrack(k, n, [], 1)
        return self.ans

    def backtrack(self, k, n, curAns, curNum):
        if k == len(curAns) and n == sum(curAns):
            self.ans.append(list(curAns))
            return
        
        if k < len(curAns) or n < sum(curAns):
            return 
        
        for num in range(curNum, 10):
            curAns.append(num)
            self.backtrack(k, n, curAns, num+1)
            curAns.pop()