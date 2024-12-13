class Node:

    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
    
class MyCircularDeque:

    def __init__(self, k: int):
        self.head = Node(-1)
        self.head.next = self.head
        self.head.prev = self.head
        self.k = k
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.size < self.k:
            newNode = Node(value)
            first = self.head.next
            first.prev = newNode
            newNode.next = first
            self.head.next = newNode
            newNode.prev = self.head
            self.size += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.size < self.k:
            newNode = Node(value)
            last = self.head.prev
            last.next = newNode
            newNode.prev = last
            newNode.next = self.head
            self.head.prev = newNode
            self.size += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.size >= 1:
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            self.size -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.size >= 1:
            self.head.prev = self.head.prev.prev
            self.head.prev.next = self.head
            self.size -= 1
            return True
        return False
        
    def getFront(self) -> int:
        return self.head.next.val
        
    def getRear(self) -> int:
        return self.head.prev.val

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