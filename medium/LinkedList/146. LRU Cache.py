class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.head.next = self.head
        self.head.prev = self.head

    def get(self, key: int) -> int:
        if not key in self.dict:
            return -1
        node = self.dict[key]
        self.remove(node)
        self.add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            oldNode = self.dict[key]
            self.remove(oldNode)
        node = Node(key, value)
        self.dict[key] = node
        self.add(node)

        if len(self.dict) > self.capacity:
            nodeDeleting = self.head.next
            self.remove(nodeDeleting)
            del self.dict[nodeDeleting.key]
    
    def add(self, node):
        last = self.head.prev
        last.next = node
        node.prev = last
        node.next = self.head
        self.head.prev = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)