class ListNode:
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.origin = ListNode(val = -1)
        self.origin.next = self.origin
        self.origin.prev = self.origin

    def enQueue(self, value: int) -> bool:
        if self.size < self.k:
            newNode = ListNode(val = value)
            self.origin.next.prev = newNode
            newNode.next = self.origin.next
            newNode.prev = self.origin
            self.origin.next = newNode
            self.size += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.size >= 1:
            self.origin.prev.prev.next = self.origin
            self.origin.prev = self.origin.prev.prev
            self.size -= 1
            return True
        return False
        
    def Front(self) -> int:
        return self.origin.prev.val

    def Rear(self) -> int:
        return self.origin.next.val

    def isEmpty(self) -> bool:
        return not self.size
        
    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()