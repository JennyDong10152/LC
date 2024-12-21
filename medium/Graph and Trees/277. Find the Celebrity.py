# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = 0
        for i in range(1, n):
            if knows(celebrity, i):
                celebrity = i
        if self.isCelebrity(celebrity, n):
            return celebrity
        return -1
    
    def isCelebrity(self, celebrity, n):
        for j in range(n):
            if celebrity == j:
                continue
            if knows(celebrity, j) or not knows(j, celebrity):
                return False
        return True