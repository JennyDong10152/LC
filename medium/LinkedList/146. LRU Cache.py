class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.head.prev = self.head
        self.head.next = self.head
        self.dict = dict()

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

        node = Node(key, value)
        self.dict[key] = node
        self.add(node)

        if len(self.dict) > self.capacity:
            nodeDelete = self.head.next
            self.remove(nodeDelete)
            del self.dict[nodeDelete.key]
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add(self, node):
        last = self.head.prev
        last.next = node
        node.prev = last
        node.next = self.head
        self.head.prev = node
    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)