class ListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if not key in self.dict:
            return -1
        node = self.dict[key]
        self.remove(node)
        self.add(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            oldNode = self.dict[key]
            self.remove(oldNode)
        
        node = ListNode(key, value)
        self.dict[key] = node
        self.add(node)

        if len(self.dict) > self.capacity:
            nodeDeleting = self.head.next
            self.remove(nodeDeleting)
            del self.dict[nodeDeleting.key]
    
    def add(self, node):
        prev_end = self.tail.prev
        prev_end.next = node
        node.prev = prev_end
        node.next = self.tail
        self.tail.prev = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)