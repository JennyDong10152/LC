class Node:

    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class FrontMiddleBackQueue:

    def __init__(self):
        self.head = Node(val=-1)
        self.head.next = self.head
        self.head.prev = self.head
        self.size = 0

    def pushFront(self, val: int) -> None:
        newNode = Node(val)
        first = self.head.next
        newNode.next = first
        first.prev = newNode
        self.head.next = newNode
        newNode.prev = self.head
        
    def pushMiddle(self, val: int) -> None:
        slow = self.head
        fast = slow.next

        while fast and fast.next and fast != self.head and fast.next != self.head:
            slow = slow.next
            fast = fast.next.next
        
        behind = slow.next
        slow.next = Node(val=val, prev=slow, next=behind)
        behind.prev = slow.next
        # print(slow.val, slow.next.val, slow.next.next.val)

    def pushBack(self, val: int) -> None:
        last = self.head.prev
        newNode = Node(val)
        last.next = newNode
        newNode.prev = last
        newNode.next = self.head
        self.head.prev = newNode
        
    def popFront(self) -> int:
        if self.head.next == self.head:
            return -1
        value = self.head.next.val
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return value
        
    def popMiddle(self) -> int:
        if self.head.next == self.head:
            return -1
            
        slow = self.head.next
        fast = slow.next

        while fast != self.head and fast.next != self.head:
            slow = slow.next
            fast = fast.next.next
        
        value = slow.val
        # previous = slow.prev
        slow.next.prev = slow.prev
        slow.prev.next = slow.next
        return value

    def popBack(self) -> int:
        if self.head.next == self.head:
            return -1
        value = self.head.prev.val
        self.head.prev = self.head.prev.prev
        self.head.prev.next = self.head
        return value


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()