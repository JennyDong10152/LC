# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = 0
        for person in range(1, n):
            if knows(celebrity, person):
                celebrity = person

        if self.isCelebrity(celebrity, n):
            return celebrity
        return -1
    
    def isCelebrity(self, celebrity, n):
        for person in range(n):
            if person == celebrity:
                continue
            if knows(celebrity, person) or not knows(person, celebrity):
                return False
        return True