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
        for i in range(n):
            if celebrity == i:
                continue
            if knows(celebrity, i) or not knows(i, celebrity):
                return False
        return True