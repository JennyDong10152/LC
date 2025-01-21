class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.answers = []
        self.search([], 1, k, n)
        return self.answers
    
    def search(self, temp, idx, k, n):
        if k < 0 or n < 0:
            return
        if not n and not k:
            self.answers.append(list(temp))
            return 
        for num in range(idx, 10):
            temp.append(num)
            self.search(temp, num+1, k-1, n-num)
            temp.pop()