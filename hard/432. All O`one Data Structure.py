class Node:

    def __init__(self, frequency):
        self.frequency = frequency
        self.prev = None
        self.next = None
        self.keys = set()
    
class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def inc(self, key: str) -> None:
        if not key in self.map:
            firstNode = self.head.next
            if firstNode == self.tail or firstNode.frequency > 1:
                newNode = Node(1)
                newNode.keys.add(key)
                newNode.prev = self.head
                self.head.next = newNode
                newNode.next = firstNode
                firstNode.prev = newNode
                self.map[key] = newNode
            else:
                firstNode.keys.add(key)
                self.map[key] = firstNode
        
        else:
            node = self.map[key]
            frequency = node.frequency
            node.keys.remove(key)
            nextNode = node.next
            if nextNode == self.tail or nextNode.frequency != frequency+1:
                newNode = Node(frequency+1)
                newNode.keys.add(key)
                newNode.prev = node
                node.next = newNode
                newNode.next = nextNode
                nextNode.prev = newNode
                self.map[key] = newNode
            else:
                nextNode.keys.add(key)
                self.map[key] = nextNode
            if not node.keys:
                self.removeNode(node)

    def dec(self, key: str) -> None:
        if key not in self.map:
            return 
        
        node = self.map[key]
        node.keys.remove(key)
        frequency = node.frequency

        if frequency == 1:
            del self.map[key]
        else:
            prevNode = node.prev
            if prevNode == self.head or prevNode.frequency != frequency-1:
                newNode = Node(frequency-1)
                newNode.keys.add(key)
                newNode.prev = prevNode
                newNode.next = node
                prevNode.next = newNode
                node.prev = newNode
                self.map[key] = newNode
            else:
                prevNode.keys.add(key)
                self.map[key] = prevNode
        if not node.keys:
            self.removeNode(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return list(self.tail.prev.keys)[0]
        

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return list(self.head.next.keys)[0]
    
    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()