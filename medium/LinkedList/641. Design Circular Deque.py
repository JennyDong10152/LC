class ListNode:

    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
    
class MyCircularDeque:

    def __init__(self, k: int):
        self.origin = ListNode(-1)
        self.origin.next = self.origin
        self.origin.prev = self.origin
        self.k = k
        self.size = 0
        
    def insertFront(self, value: int) -> bool:
        if self.size < self.k:
            newNode = ListNode(val=value)
            self.origin.next.prev = newNode
            newNode.next = self.origin.next
            newNode.prev = self.origin
            self.origin.next = newNode
            self.size += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.size < self.k:
            newNode = ListNode(val=value)
            self.origin.prev.next = newNode
            newNode.prev = self.origin.prev
            newNode.next = self.origin
            self.origin.prev = newNode
            self.size += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.size >= 1:
            self.origin.next = self.origin.next.next
            self.origin.next.prev = self.origin
            self.size -= 1
            return True
        return False
        
    def deleteLast(self) -> bool:
        if self.size >= 1:
            self.origin.prev = self.origin.prev.prev
            self.origin.prev.next = self.origin
            self.size -= 1
            return True
        return False
        
    def getFront(self) -> int:
        return self.origin.next.val

    def getRear(self) -> int:
        return self.origin.prev.val

    def isEmpty(self) -> bool:
        return not self.size
        
    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()