class Node:

    def __init__(self, val=0, prev= None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = Node(-1)
        self.head.next = self.head
        self.head.prev = self.head
        self.k = k
        self.size = 0
        
    def enQueue(self, value: int) -> bool:
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

    def deQueue(self) -> bool:
        if self.size >= 1:
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            self.size -= 1
            return True
        return False

    def Front(self) -> int:
        return self.head.next.val
        

    def Rear(self) -> int:
        return self.head.prev.val
        
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