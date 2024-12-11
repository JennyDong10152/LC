class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if self.size <= index or index < 0:
            return -1

        node = self.dummy.next
        for _ in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val, self.dummy.next)
        self.dummy.next = node
        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        node = self.dummy
        while node.next:
            node = node.next
        node.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        node = self.dummy
        for _ in range(index):
            node = node.next
        node.next = ListNode(val, node.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        node = self.dummy
        for _ in range(index):
            node = node.next
        node.next = node.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)