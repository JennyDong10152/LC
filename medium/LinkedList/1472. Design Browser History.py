class Node:

    def __init__(self, url="", prev=None, next=None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.size = 1
        
    def visit(self, url: str) -> None:
        newNode = Node(url)
        self.head.next = newNode
        newNode.prev = self.head
        self.head = self.head.next

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.head.prev:
                break
            self.head = self.head.prev
        return self.head.url

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.head.next:
                break
            self.head = self.head.next
        return self.head.url