class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = Node(-1)
        self.size = 0

    def get(self, index: int) -> int:
        if 0 <= index < self.size:
            current = self.dummy
            for _ in range(index+1):
                current = current.next
            return current.val
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.dummy.next)
        self.dummy.next = node
        self.size += 1        


    def addAtTail(self, val: int) -> None:
        current = self.dummy
        while current.next:
            current = current.next
        current.next = Node(val)
        self.size += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        current = self.dummy
        if 0 <= index <= self.size:
            for _ in range(index):
                current = current.next
            current.next = Node(val, current.next)
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.size:
            current = self.dummy
            for _ in range(index):
                current = current.next
            current.next = current.next.next
            self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)